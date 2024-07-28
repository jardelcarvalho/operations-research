import sys
sys.path.append('../../utils')

import set_operations

import pyomo.environ as pyo
import numpy as np

DATA = {'graph': None, 'Pi': None}

class _Constants:
    lambda_ = None
    K = None
    
    def initialize(lambda_, K):
        _Constants.lambda_ = lambda_
        _Constants.K = K

class _VariableIndexFormating:
    def rho(i, pi):
        return f'Node({i})_Partition({pi})'

    def epsilon(i, j):
        if i < j:
            return f'Edge({i}, {j})'
        return f'Edge({j}, {i})'

    def kappa(sign):
        return f'Sign({sign})'

    def xi(i, j, pi):
        return f'Node({i})_Node({j})_Partition({pi})'

    def psi(i, j, k):
        if j == k:
            #epsilon(1, 2) * epsilon(1, 2) = epsilon(2, 1) * epsilon(2, 1)
            #psi(1, 2, 2) = epsilon(1, 2) * epsilon(1, 2)
            #psi(2, 1, 1) = epsilon(2, 1) * epsilon(2, 1)
            #So psi(1, 2, 2) = psi(2, 1, 1)
            min_ = min(i, j, k)
            max_ = max(i, j, k)
            return f'Node({min_})_Node({max_})_Node({max_})'
        return f'Node({i})_Node({j})_Node({k})'

class _ExpressionTerms:
    def __init__(self):
        self.variables = {}
        self.constants = []

    def __str__(self):
        terms = []
        for name in self.variables:
            for index, coef in self.variables[name]:
                terms.append(f'{coef}{name}_{index}')

        for c in self.constants:
            terms.append(str(c))

        return ' + '.join(terms)

    def __repr__(self):
        return self.__str__()

    @property
    def variables_names(self):
        return list(self.variables.keys())

    def add_variable(self, name, index, coef):
        if name not in self.variables:
            self.variables[name] = []
        self.variables[name].append((index, coef))

    def add_constant(self, value):
        self.constants.append(value)

class _ConstraintsSet:
    def __init__(self, signal):
        if signal == '<':
            self.operation = lambda lhs, rhs: lhs < rhs
        elif signal == '>':
            self.operation = lambda lhs, rhs: lhs > rhs
        elif signal == '<=':
            self.operation = lambda lhs, rhs: lhs <= rhs
        elif signal == '>=':
            self.operation = lambda lhs, rhs: lhs >= rhs
        elif signal == '==':
            self.operation = lambda lhs, rhs: lhs == rhs
        else:
            raise Exception(f'Invalid signal: {signal}')
        self.signal = signal
        self.constraints = {}

    def __getitem__(self, constraint_index):
        if constraint_index not in self.constraints:
            self.constraints[constraint_index] = {'rhs': _ExpressionTerms(), 'lhs': _ExpressionTerms()}
        return self.constraints[constraint_index]

    def __str__(self):
        lines = ''
        for constraint_index in self.constraints:
            lines += (
                f"{constraint_index}:\t"\
                f"{self.constraints[constraint_index]['lhs'].__str__()} "\
                f"{self.signal} "\
                f"{self.constraints[constraint_index]['rhs'].__str__()}\n")
        return lines

    def __repr__(self):
        return self.__str__()

def get_grouped_variables_indices(objective, constraints_set_list):
    expressions = [objective]
    for constraints_set in constraints_set_list:
        for constraint_index in constraints_set.constraints:
            expressions.append(constraints_set.constraints[constraint_index]['lhs'])
            expressions.append(constraints_set.constraints[constraint_index]['rhs'])

    variables = {}
    for expr in expressions:
        for name in expr.variables:
            if name not in variables:
                variables[name] = set()
            for index, _ in expr.variables[name]:
                variables[name] |= {index}

    return variables

class _DecomposedModelStructure:
    def objective():
        objective = _ExpressionTerms()

        for i, j, weight in DATA['graph'].edges:
            objective.add_variable('epsilon', _VariableIndexFormating.epsilon(i, j), weight)
        
        objective.add_constant(_Constants.K * _Constants.lambda_)
        objective.add_variable('kappa', _VariableIndexFormating.kappa('-'), -_Constants.lambda_)
        objective.add_variable('kappa', _VariableIndexFormating.kappa('+'), -_Constants.lambda_) 

        return objective

    def c1():
        constraint_set = _ConstraintsSet('<=')

        for i in DATA['graph'].nodes:
            for pi in DATA['Pi']:
                constraint_set[f'Node({i})']['lhs'].add_variable('rho', _VariableIndexFormating.rho(i, pi), 1)
            constraint_set[f'Node({i})']['rhs'].add_constant(1)

        return constraint_set

    def c2():
        constraint_set = _ConstraintsSet('<=')

        for pi in DATA['Pi']:
            for i in DATA['graph'].nodes:
                constraint_set[f'Partition({pi})']['lhs'].add_variable('rho', _VariableIndexFormating.rho(i, pi), 1)
            constraint_set[f'Partition({pi})']['rhs'].add_constant(1)

        return constraint_set

    def c3():
        constraint_set = _ConstraintsSet('==')

        for pi in DATA['Pi']:
            for i in DATA['graph'].nodes:
                constraint_set['Unique']['lhs'].add_variable(
                    'rho', _VariableIndexFormating.rho(i, pi), 1)

        constraint_set['Unique']['lhs'].add_variable('kappa', _VariableIndexFormating.kappa('-'), 1)
        constraint_set['Unique']['lhs'].add_variable('kappa', _VariableIndexFormating.kappa('+'), -1)
        constraint_set['Unique']['rhs'].add_constant(_Constants.K)

        return constraint_set

    def c4():
        constraint_set = _ConstraintsSet('<=')

        constraint_set['Unique']['lhs'].add_variable('kappa', _VariableIndexFormating.kappa('-'), 1)
        constraint_set['Unique']['lhs'].add_variable('kappa', _VariableIndexFormating.kappa('+'), 1)
        constraint_set['Unique']['rhs'].add_constant(_Constants.K)

        return constraint_set

    def c5():
        constraint_set = _ConstraintsSet('==')

        for i in DATA['graph'].nodes:
            constraint_set[f'Node({i})']['lhs'].add_constant(1)
            for pi in DATA['Pi']:
                constraint_set[f'Node({i})']['lhs'].add_variable('rho', _VariableIndexFormating.rho(i, pi), -1)
            for j in DATA['graph'].neighborhoods(i):
                for pi in DATA['Pi']:
                    constraint_set[f'Node({i})']['rhs'].add_variable('xi', _VariableIndexFormating.xi(i, j, pi), 1)
            
        return constraint_set

    def c6():
        constraint_set = _ConstraintsSet('==')

        for i, j, _ in DATA['graph'].edges:
            intersection = set_operations.intersection([
                DATA['graph'].neighborhoods(i), DATA['graph'].neighborhoods(j)])
            
            for k in intersection:
                constraint_set[f'Edge({i}, {j})']['lhs'].add_variable('psi', _VariableIndexFormating.psi(i, j, k), 1)
                constraint_set[f'Edge({i}, {j})']['lhs'].add_variable('psi', _VariableIndexFormating.psi(j, i, k), 1)

            for k in DATA['graph'].neighborhoods(i):
                constraint_set[f'Edge({i}, {j})']['rhs'].add_variable('psi', _VariableIndexFormating.psi(i, j, k), 1)

            for k in DATA['graph'].neighborhoods(j):
                constraint_set[f'Edge({i}, {j})']['rhs'].add_variable('psi', _VariableIndexFormating.psi(j, i, k), 1)

            constraint_set[f'Edge({i}, {j})']['rhs'].add_variable('epsilon', _VariableIndexFormating.epsilon(i, j), 2)

        return constraint_set
        
    def c7():
        constraint_set = _ConstraintsSet('==')

        for i, j, _ in DATA['graph'].edges:
            intersection = set_operations.intersection([
                DATA['graph'].neighborhoods(i), DATA['graph'].neighborhoods(j)])

            for k in intersection:
                constraint_set[f'Edge({i}, {j})']['lhs'].add_variable('psi', _VariableIndexFormating.psi(i, j, k), 1)

            for k in intersection:
                constraint_set[f'Edge({i}, {j})']['rhs'].add_variable('psi', _VariableIndexFormating.psi(j, i, k), 1)

        return constraint_set

    def c8():
        constraint_set = _ConstraintsSet('==')

        for i, j, _ in DATA['graph'].edges:
            for k in DATA['graph'].neighborhoods(i):
                constraint_set[f'Edge({i}, {j})']['lhs'].add_variable('psi', _VariableIndexFormating.psi(i, j, k), 1)

            for k in DATA['graph'].neighborhoods(j):
                constraint_set[f'Edge({i}, {j})']['rhs'].add_variable('psi', _VariableIndexFormating.psi(j, i, k), 1)

        return constraint_set

def initialize(graph, Pi):
    DATA['graph'] = graph
    DATA['Pi'] = Pi

    _Constants.initialize(sum(w for _, _, w in DATA['graph'].edges), len(DATA['Pi']))

    objective = _DecomposedModelStructure.objective()
    c1 = _DecomposedModelStructure.c1()
    c2 = _DecomposedModelStructure.c2()
    c3 = _DecomposedModelStructure.c3()
    c4 = _DecomposedModelStructure.c4()
    c5 = _DecomposedModelStructure.c5()
    c6 = _DecomposedModelStructure.c6()
    c7 = _DecomposedModelStructure.c7()
    c8 = _DecomposedModelStructure.c8()

    all_variables_indices = get_grouped_variables_indices(objective, [c1, c2, c3, c4, c5, c6, c7, c8])

    for name in all_variables_indices:
        print(f'{name}:\t', '  '.join(all_variables_indices[name]), sep='', end='\n\n')


'''
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

def psi(i, j, k):
    return _model.psi[psi_index(i, j, k)]
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

def psi_index(i, j, k):
    return f'{i}_{j}_{k}'
#endregion variable indexation

#region model creation
_model = None

def _set_linearization_variables_xi():
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

    _model.xi_linearization_constraint_xi_1 = pyo.Constraint(
        list(range(len(xi_indices))), rule=lambda _, idx: get_constraints(idx, 'c1'))
    _model.xi_linearization_constraint_xi_2 = pyo.Constraint(
        list(range(len(xi_indices))), rule=lambda _, idx: get_constraints(idx, 'c2'))
    _model.xi_linearization_constraint_xi_3 = pyo.Constraint(
        list(range(len(xi_indices))), rule=lambda _, idx: get_constraints(idx, 'c3'))

def _set_linearization_variables_psi():
    psi_indices = []
    for i, j in E:
        psi_indices.extend(cart([[i], [j], n(i)], ravel=True))

    _model.psi = pyo.Var(list(map(lambda t: psi_index(*t), psi_indices)), within=pyo.Binary)

    def get_constraints(idx, c):
        i, j, k = psi_indices[idx]
        if c == 'c1':
            return psi(i, j, k) <= epsilon(i, j)
        elif c == 'c2':
            return psi(i, j, k) <= epsilon(j, k)
        else:
            return psi(i, j, k) >= epsilon(i, j) + epsilon(j, k) - 1

    _model.xi_linearization_constraint_psi_1 = pyo.Constraint(
        list(range(len(psi_indices))), rule=lambda _, idx: get_constraints(idx, 'c1'))
    _model.xi_linearization_constraint_psi_2 = pyo.Constraint(
        list(range(len(psi_indices))), rule=lambda _, idx: get_constraints(idx, 'c2'))
    _model.xi_linearization_constraint_psi_3 = pyo.Constraint(
        list(range(len(psi_indices))), rule=lambda _, idx: get_constraints(idx, 'c3'))

def _set_variables():
    _model.rho = pyo.Var(list(map(lambda t: rho_index(*t), cart([V, Pi]))), within=pyo.Binary)
    _model.epsilon = pyo.Var(list(map(lambda t: epsilon_index(*t), E)), within=pyo.Binary)
    _model.kappa = pyo.Var(list(map(kappa_index, ['neg', 'pos'])), within=pyo.PositiveReals)
    _set_linearization_variables_xi()
    _set_linearization_variables_psi()

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

    for i, j in E:
        print(i, j, epsilon(i, j)())

    print()
    for i in V:
        for pi in Pi:
            print(i, pi, rho(i, pi)())

    print(status)

'''