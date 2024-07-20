import pyomo.environ as pyo
import numpy as np

#region model constants
lamb = None
K = None

def _compute_lamb(graph):
    r = 0
    for n in graph.nodes:
        for neighborhood in graph.neighborhoods(n):
            r += graph[n, neighborhood]
    return r

def _set_model_constants(graph, _K):
    global lamb
    global K

    K = _K
    lamb = _compute_lamb(graph)
#endregion model constants

#region model sets
V = None
E = None
Pi = None

def _set_model_sets(graph, K):
    global V
    global E
    global Pi

    V = graph.nodes
    E = graph.edges
    Pi = list(range(K))
#endregion model sets

#region model functions
n = None
omega = None

def cart(sets, ravel=False):
    res = sets[0]
    for i in range(1, len(sets)):
        new = []
        for a in res:
            for b in sets[i]:
                if ravel:
                    new_a = [a]
                    if isinstance(a, (set, tuple)):
                        new_a = list(a)
                    new_b = [b]
                    if isinstance(b, (set, tuple)):
                        new_b = list(b)
                    new.append(tuple(new_a + new_b))
                else:
                    new.append((a, b))
        res = new
    return res

def intersection(sets):
    res = set()
    minor_set, _ = min(list(map(lambda s: (s, len(s)), sets)), key=lambda t: t[1])
    for e in minor_set:
        intersects_all = True
        for other_set in sets:
            if e not in other_set:
                intersects_all = False
                break
        if intersects_all:
            res.add(e)
    return list(res)

def _set_model_functions(graph, _):
    global n
    global omega

    def func_n(i):
        return graph.neighborhoods(i)

    def func_omega(i, j):
        return graph[i, j]
        
    n = func_n
    omega = func_omega
#endregion model functions

#region model variables
def rho(i, pi):
    return _model.rho[rho_index(i, pi)]

def epsilon(i, j):
    return _model.epsilon[epsilon_index(i, j)]

def kappa(sign):
    return _model.kappa[kappa_index(sign)]

def xi(i, j, pi):
    return _model.xi[xi_index(i, j, pi)]
#endregion model variables

#region variable indexation
def rho_index(i, pi):
    return f'{i}_{pi}'

def epsilon_index(i, j):
    return f'{i}_{j}'

def kappa_index(sign):
    return f'{sign}'

def xi_index(i, j, pi):
    return f'{i}_{j}_{pi}'
#endregion variable indexation

#region model creation
_model = None

def _set_linearization_variables():
    xi_indices = []
    for i in V:
        xi_indices.extend(cart([[i], n(i), Pi], ravel=True))

    _model.xi = pyo.Var(list(map(lambda t: xi_index(*t), xi_indices)), within=pyo.Binary)

    def get_constraints(idx, c):
        i, j, pi = xi_indices[idx]
        if c == 'c1':
            return xi(i, j, pi) <= epsilon(i, j)
        elif c == 'c2':
            return xi(i, j, pi) <= rho(j, pi)
        else:
            return xi(i, j, pi) >= epsilon(i, j) + rho(j, pi) - 1

    _model.xi_linearization_constraint1 = pyo.Constraint(
        list(range(len(xi_indices))), rule=lambda _, idx: get_constraints(idx, 'c1'))
    _model.xi_linearization_constraint2 = pyo.Constraint(
        list(range(len(xi_indices))), rule=lambda _, idx: get_constraints(idx, 'c2'))
    _model.xi_linearization_constraint3 = pyo.Constraint(
        list(range(len(xi_indices))), rule=lambda _, idx: get_constraints(idx, 'c3'))

def _set_variables():
    _model.rho = pyo.Var(list(map(lambda t: rho_index(*t), cart([V, Pi]))), within=pyo.Binary)
    _model.epsilon = pyo.Var(list(map(lambda t: epsilon_index(*t), E)), within=pyo.Binary)
    _model.kappa = pyo.Var(list(map(kappa_index, ['neg', 'pos'])), within=pyo.PositiveReals)
    _set_linearization_variables()

def _set_objective():
    z = sum(map(lambda idx: omega(*idx) * epsilon(*idx), E)) + (K - kappa('neg') - kappa('pos')) * lamb
    _model.z = pyo.Objective(expr=z, sense=pyo.minimize)

def _set_constraint1():
    def lhs(i):
        return sum(map(lambda pi: rho(i, pi), Pi))
    _model.vertex_represents_unique_partition = pyo.Constraint(V, rule=lambda _, i: lhs(i) <= 1)

def _set_constraint2():
    def lhs(pi):
        return sum(map(lambda i: rho(i, pi), V))
    _model.partition_has_unique_representant = pyo.Constraint(Pi, rule=lambda _, pi: lhs(pi) <= 1)

def _set_constraint3():
    def lhs():
        res = 0
        for pi in Pi:
            for i in V:
                res += rho(i, pi)
        return res

    _model.relaxation_total_components = pyo.Constraint(
        rule=lambda _: lhs() + kappa('neg') - kappa('pos') == 0)

def _set_constraint4():
    _model.max_kappa = pyo.Constraint(
        rule=lambda _: kappa('neg') + kappa('pos') <= K)

def _set_constraint5():
    def lhs(i):
        return 1 - sum(rho(i, pi) for pi in Pi)
    
    def rhs(i):
        return sum(xi(*arg) for arg in cart([[i], n(i), Pi], ravel=True))
    
    _model.representants_and_non_representants_relationship = pyo.Constraint(V, rule=lambda _, i: lhs(i) == rhs(i))

def _set_constraint6():
    def lhs(idx):
        i, j = E[idx]
        res = (len(n(i)) + len(n(j))) * (1 - epsilon(i, j))
        for k in intersection([n(i), n(j)]):
            res += epsilon(i, k) + epsilon(j, k)
        return res
    
    def rhs(idx):
        i, j = E[idx]

        res = 0
        for k in n(i):
            res += epsilon(i, k)
        
        for k in n(j):
            res += epsilon(j, k)

        res -= 2
        return res

    indices = range(len(E))
    _model.strongly_connected_components = pyo.Constraint(indices, rule=lambda _, idx: lhs(idx) >= rhs(idx))

def _create_model():
    global _model

    _model = pyo.ConcreteModel()

    _set_variables()
    _set_objective()
    _set_constraint1()
    _set_constraint2()
    _set_constraint3()
    _set_constraint4()
    _set_constraint5()
    _set_constraint6()

    _model.write('lp.lp', io_options={'symbolic_solver_labels': True})
#endregion model creation

def initialize(graph, K, lp_file_path=None):
    global _model

    _set_model_constants(graph, K)
    _set_model_sets(graph, K)
    _set_model_functions(graph, K)

    # print(K)
    # print(phi)
    # print(V)
    # print(E)
    # print(Pi)
    # print(n(1))
    # print(omega(1, 4))

    _create_model()

def run():
    solver = pyo.SolverFactory('cbc', executable='../../solvers/Cbc/bin/cbc.exe')
    solver.options['LogFile'] = 'log.log'

    status = solver.solve(_model, options={"threads": 8})

    print(status)