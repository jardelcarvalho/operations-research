from lib.data import DATA

import sys
sys.path.append('../../utils')
import set_operations
from expressions_decomposition import ExpressionTerms, ConstraintsSet

class VariableIndexFormating:
    def x(i, j):
        if i < j:
            return f'Edge({i}, {j})'
        return f'Edge({j}, {i})'

    def rho(i, j, k):
        if j == k:
            #x(1, 2) * x(1, 2) = x(2, 1) * x(2, 1)
            #rho(1, 2, 2) = x(1, 2) * x(1, 2)
            #rho(2, 1, 1) = x(2, 1) * x(2, 1)
            #rho(1, 2, 2) = rho(2, 1, 1)
            min_ = min(i, j, k)
            max_ = max(i, j, k)
            return f'Node({min_})_Node({max_})_Node({max_})'
        return f'Node({i})_Node({j})_Node({k})'

class DecomposedModelStructure:
    def objective():
        objective = ExpressionTerms()

        for i, j, weight in DATA['graph'].edges:
            objective.add_variable('x', VariableIndexFormating.x(i, j), weight / 2)

        for i, j, weight in DATA['graph'].edges:
            objective.add_variable('x', VariableIndexFormating.x(i, j), -weight)

        for i, j, weight in DATA['graph'].edges:
            objective.add_constant(weight) 

        return objective

    def c1():
        constraint_set = ConstraintsSet('==')

        for i, j, _ in DATA['graph'].edges:
            intersection = set_operations.intersection([
                DATA['graph'].neighborhoods(i), DATA['graph'].neighborhoods(j)])
            
            for k in intersection:
                constraint_set[f'Edge({i}, {j})']['lhs'].add_variable('rho', VariableIndexFormating.rho(i, j, k), 1)
                constraint_set[f'Edge({i}, {j})']['lhs'].add_variable('rho', VariableIndexFormating.rho(j, i, k), 1)

            for k in DATA['graph'].neighborhoods(i):
                constraint_set[f'Edge({i}, {j})']['rhs'].add_variable('rho', VariableIndexFormating.rho(i, j, k), 1)

            for k in DATA['graph'].neighborhoods(j):
                constraint_set[f'Edge({i}, {j})']['rhs'].add_variable('rho', VariableIndexFormating.rho(j, i, k), 1)

            constraint_set[f'Edge({i}, {j})']['rhs'].add_variable('x', VariableIndexFormating.x(i, j), -2)

        return constraint_set
        
    def c2():
        constraint_set = ConstraintsSet('==')

        for i, j, _ in DATA['graph'].edges:
            intersection = set_operations.intersection([
                DATA['graph'].neighborhoods(i), DATA['graph'].neighborhoods(j)])

            for k in intersection:
                constraint_set[f'Edge({i}, {j})']['lhs'].add_variable('rho', VariableIndexFormating.rho(i, j, k), 1)

            for k in intersection:
                constraint_set[f'Edge({i}, {j})']['rhs'].add_variable('rho', VariableIndexFormating.rho(j, i, k), 1)

        return constraint_set

    def c3():
        constraint_set = ConstraintsSet('==')

        for i, j, _ in DATA['graph'].edges:
            for k in DATA['graph'].neighborhoods(i):
                constraint_set[f'Edge({i}, {j})']['lhs'].add_variable('rho', VariableIndexFormating.rho(i, j, k), 1)

            for k in DATA['graph'].neighborhoods(j):
                constraint_set[f'Edge({i}, {j})']['rhs'].add_variable('rho', VariableIndexFormating.rho(j, i, k), 1)

        return constraint_set

    def c4_rho_linearization():
        constraint_set_leq_x1 = ConstraintsSet('<=')
        constraint_set_leq_x2 = ConstraintsSet('<=')
        constraint_set_geq = ConstraintsSet('>=')

        for i, j, _ in DATA['graph'].edges:
            for k in DATA['graph'].neighborhoods(i):
                constraint_set_leq_x1[f'rho_product({i}, {j}, {k})']['lhs'].add_variable('rho', VariableIndexFormating.rho(i, j, k), 1)
                constraint_set_leq_x1[f'rho_product({i}, {j}, {k})']['rhs'].add_variable('x', VariableIndexFormating.x(i, j), 1)

                constraint_set_leq_x2[f'rho_product({i}, {j}, {k})']['lhs'].add_variable('rho', VariableIndexFormating.rho(i, j, k), 1)
                constraint_set_leq_x2[f'rho_product({i}, {j}, {k})']['rhs'].add_variable('x', VariableIndexFormating.x(i, k), 1)

                constraint_set_geq[f'rho_product({i}, {j}, {k})']['lhs'].add_variable('rho', VariableIndexFormating.rho(i, j, k), 1)
                constraint_set_geq[f'rho_product({i}, {j}, {k})']['rhs'].add_variable('x', VariableIndexFormating.x(i, j), 1)
                constraint_set_geq[f'rho_product({i}, {j}, {k})']['rhs'].add_variable('x', VariableIndexFormating.x(i, k), 1)
                constraint_set_geq[f'rho_product({i}, {j}, {k})']['rhs'].add_constant(-1)

            for k in DATA['graph'].neighborhoods(j):
                constraint_set_leq_x1[f'rho_product({j}, {i}, {k})']['lhs'].add_variable('rho', VariableIndexFormating.rho(j, i, k), 1)
                constraint_set_leq_x1[f'rho_product({j}, {i}, {k})']['rhs'].add_variable('x', VariableIndexFormating.x(j, i), 1)

                constraint_set_leq_x2[f'rho_product({j}, {i}, {k})']['lhs'].add_variable('rho', VariableIndexFormating.rho(j, i, k), 1)
                constraint_set_leq_x2[f'rho_product({j}, {i}, {k})']['rhs'].add_variable('x', VariableIndexFormating.x(j, k), 1)

                constraint_set_geq[f'rho_product({j}, {i}, {k})']['lhs'].add_variable('rho', VariableIndexFormating.rho(j, i, k), 1)
                constraint_set_geq[f'rho_product({j}, {i}, {k})']['rhs'].add_variable('x', VariableIndexFormating.x(j, i), 1)
                constraint_set_geq[f'rho_product({j}, {i}, {k})']['rhs'].add_variable('x', VariableIndexFormating.x(j, k), 1)
                constraint_set_geq[f'rho_product({j}, {i}, {k})']['rhs'].add_constant(-1)

        return constraint_set_leq_x1, constraint_set_leq_x2, constraint_set_geq


