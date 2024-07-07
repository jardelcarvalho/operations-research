import pyomo.environ as pyo
import numpy as np

#region model constants
phi = None
K = None

def _compute_phi(graph):
    r = 0
    for n in graph.nodes:
        for neighborhood in graph.neighborhoods(n):
            r += graph[n, neighborhood]
    return r

def _set_model_constants(graph, _K):
    global phi
    global K

    K = _K
    phi = _compute_phi(graph)
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

def s(sign):
    return _model.s[s_index(sign)]
#endregion model variables

#region variable indexation
def rho_index(i, pi):
    return f'{i}_{pi}'

def epsilon_index(i, j):
    return f'{i}_{j}'

def s_index(sign):
    return f'{sign}'
#endregion variable indexation

#region model creation
_model = None

def _set_variables():
    _model.rho = pyo.Var(list(map(lambda t: rho_index(*t), cart([V, Pi]))), within=pyo.Binary)
    _model.epsilon = pyo.Var(list(map(lambda t: epsilon_index(*t), E)), within=pyo.Binary)
    _model.s = pyo.Var(list(map(s_index, ['neg', 'pos'])), within=pyo.PositiveReals)

def _set_objective():
    z = sum(map(lambda idx: omega(*idx) * epsilon(*idx), E)) + (K - s('neg') - s('pos')) * phi
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
    VxPi = cart([V, Pi])

    def lhs(idx):
        i, pi = VxPi[idx]
        return sum(map(lambda j: rho(j, pi), range(1, i)))

    _model.min_index_representant = pyo.Constraint(list(range(len(VxPi))), lambda _, idx: lhs(idx) == 0)

def _set_constraint4():
    pass

def _set_constraint5():
    pass

def _set_constraint6():
    pass

def _create_model():
    global _model

    _model = pyo.ConcreteModel()

    _set_variables()
    _set_objective()
    # _set_constraint1()
    # _set_constraint2()
    _set_constraint3()
    # _set_constraint4()
    # _set_constraint5()
    # _set_constraint6()

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
    pass