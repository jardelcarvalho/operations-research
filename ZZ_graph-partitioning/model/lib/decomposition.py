from lib.data import Constants, DATA

import sys
sys.path.append('../../utils')
import set_operations
from expressions_decomposition import ExpressionTerms, ConstraintsSet

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
            #psi(1, 2, 2) = psi(2, 1, 1)
            min_ = min(i, j, k)
            max_ = max(i, j, k)
            return f'Node({min_})_Node({max_})_Node({max_})'
        return f'Node({i})_Node({j})_Node({k})'

class DecomposedModelStructure:
    def objective():
        objective = ExpressionTerms()

        for i, j, weight in DATA['graph'].edges:
            objective.add_variable('epsilon', _VariableIndexFormating.epsilon(i, j), weight)
        
        objective.add_variable('kappa', _VariableIndexFormating.kappa('neg'), Constants.lambda_)
        objective.add_variable('kappa', _VariableIndexFormating.kappa('pos'), Constants.lambda_) 

        return objective

    def c1():
        constraint_set = ConstraintsSet('<=')

        for i in DATA['graph'].nodes:
            for pi in DATA['Pi']:
                constraint_set[f'Node({i})']['lhs'].add_variable('rho', _VariableIndexFormating.rho(i, pi), 1)
            constraint_set[f'Node({i})']['rhs'].add_constant(1)

        return constraint_set

    def c2():
        constraint_set = ConstraintsSet('<=')

        for pi in DATA['Pi']:
            for i in DATA['graph'].nodes:
                constraint_set[f'Partition({pi})']['lhs'].add_variable('rho', _VariableIndexFormating.rho(i, pi), 1)
            constraint_set[f'Partition({pi})']['rhs'].add_constant(1)

        return constraint_set

    def c3():
        constraint_set = ConstraintsSet('==')

        for pi in DATA['Pi']:
            for i in DATA['graph'].nodes:
                constraint_set['Unique']['lhs'].add_variable('rho', _VariableIndexFormating.rho(i, pi), 1)

        constraint_set['Unique']['lhs'].add_variable('kappa', _VariableIndexFormating.kappa('neg'), 1)
        constraint_set['Unique']['lhs'].add_variable('kappa', _VariableIndexFormating.kappa('pos'), -1)
        constraint_set['Unique']['rhs'].add_constant(Constants.K)

        return constraint_set

    def c4():
        constraint_set = ConstraintsSet('<=')

        constraint_set['Unique']['lhs'].add_variable('kappa', _VariableIndexFormating.kappa('neg'), 1)
        constraint_set['Unique']['lhs'].add_variable('kappa', _VariableIndexFormating.kappa('pos'), 1)

        constraint_set['Unique']['rhs'].add_constant(Constants.K)
        for pi in DATA['Pi']:
            for i in DATA['graph'].nodes:
                constraint_set['Unique']['rhs'].add_variable('rho', _VariableIndexFormating.rho(i, pi), -1)

        return constraint_set

    def c5():
        constraint_set = ConstraintsSet('==')

        for i in DATA['graph'].nodes:
            constraint_set[f'Node({i})']['lhs'].add_constant(1)
            for pi in DATA['Pi']:
                constraint_set[f'Node({i})']['lhs'].add_variable('rho', _VariableIndexFormating.rho(i, pi), -1)
            for j in DATA['graph'].neighborhoods(i):
                for pi in DATA['Pi']:
                    constraint_set[f'Node({i})']['rhs'].add_variable('xi', _VariableIndexFormating.xi(i, j, pi), 1)
            
        return constraint_set

    def c6():
        constraint_set = ConstraintsSet('==')

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

            constraint_set[f'Edge({i}, {j})']['rhs'].add_variable('epsilon', _VariableIndexFormating.epsilon(i, j), -2)

        return constraint_set
        
    def c7():
        constraint_set = ConstraintsSet('==')

        for i, j, _ in DATA['graph'].edges:
            intersection = set_operations.intersection([
                DATA['graph'].neighborhoods(i), DATA['graph'].neighborhoods(j)])

            for k in intersection:
                constraint_set[f'Edge({i}, {j})']['lhs'].add_variable('psi', _VariableIndexFormating.psi(i, j, k), 1)

            for k in intersection:
                constraint_set[f'Edge({i}, {j})']['rhs'].add_variable('psi', _VariableIndexFormating.psi(j, i, k), 1)

        return constraint_set

    def c8():
        constraint_set = ConstraintsSet('==')

        for i, j, _ in DATA['graph'].edges:
            for k in DATA['graph'].neighborhoods(i):
                constraint_set[f'Edge({i}, {j})']['lhs'].add_variable('psi', _VariableIndexFormating.psi(i, j, k), 1)

            for k in DATA['graph'].neighborhoods(j):
                constraint_set[f'Edge({i}, {j})']['rhs'].add_variable('psi', _VariableIndexFormating.psi(j, i, k), 1)

        return constraint_set

    def c9_xi_linearization():
        constraint_set_leq_epsilon = ConstraintsSet('<=')
        constraint_set_leq_rho = ConstraintsSet('<=')
        constraint_set_geq = ConstraintsSet('>=')

        for i in DATA['graph'].nodes:
            for j in DATA['graph'].neighborhoods(i):
                for pi in DATA['Pi']:
                    constraint_set_leq_epsilon[f'xi_product({i}, {j}, {pi})']['lhs'].add_variable('xi', _VariableIndexFormating.xi(i, j, pi), 1)
                    constraint_set_leq_epsilon[f'xi_product({i}, {j}, {pi})']['rhs'].add_variable('epsilon', _VariableIndexFormating.epsilon(i, j), 1)

                    constraint_set_leq_rho[f'xi_product({i}, {j}, {pi})']['lhs'].add_variable('xi', _VariableIndexFormating.xi(i, j, pi), 1)
                    constraint_set_leq_rho[f'xi_product({i}, {j}, {pi})']['rhs'].add_variable('rho', _VariableIndexFormating.rho(j, pi), 1)

                    constraint_set_geq[f'xi_product({i}, {j}, {pi})']['lhs'].add_variable('xi', _VariableIndexFormating.xi(i, j, pi), 1)
                    constraint_set_geq[f'xi_product({i}, {j}, {pi})']['rhs'].add_variable('epsilon', _VariableIndexFormating.epsilon(i, j), 1)
                    constraint_set_geq[f'xi_product({i}, {j}, {pi})']['rhs'].add_variable('rho', _VariableIndexFormating.rho(j, pi), 1)
                    constraint_set_geq[f'xi_product({i}, {j}, {pi})']['rhs'].add_constant(-1)
                
        return constraint_set_leq_epsilon, constraint_set_leq_rho, constraint_set_geq

    def c10_psi_linearization():
        constraint_set_leq_epsilon1 = ConstraintsSet('<=')
        constraint_set_leq_epsilon2 = ConstraintsSet('<=')
        constraint_set_geq = ConstraintsSet('>=')

        for i, j, _ in DATA['graph'].edges:
            for k in DATA['graph'].neighborhoods(i):
                constraint_set_leq_epsilon1[f'psi_product({i}, {j}, {k})']['lhs'].add_variable('psi', _VariableIndexFormating.psi(i, j, k), 1)
                constraint_set_leq_epsilon1[f'psi_product({i}, {j}, {k})']['rhs'].add_variable('epsilon', _VariableIndexFormating.epsilon(i, j), 1)

                constraint_set_leq_epsilon2[f'psi_product({i}, {j}, {k})']['lhs'].add_variable('psi', _VariableIndexFormating.psi(i, j, k), 1)
                constraint_set_leq_epsilon2[f'psi_product({i}, {j}, {k})']['rhs'].add_variable('epsilon', _VariableIndexFormating.epsilon(i, k), 1)

                constraint_set_geq[f'psi_product({i}, {j}, {k})']['lhs'].add_variable('psi', _VariableIndexFormating.psi(i, j, k), 1)
                constraint_set_geq[f'psi_product({i}, {j}, {k})']['rhs'].add_variable('epsilon', _VariableIndexFormating.epsilon(i, j), 1)
                constraint_set_geq[f'psi_product({i}, {j}, {k})']['rhs'].add_variable('epsilon', _VariableIndexFormating.epsilon(i, k), 1)
                constraint_set_geq[f'psi_product({i}, {j}, {k})']['rhs'].add_constant(-1)

            for k in DATA['graph'].neighborhoods(j):
                constraint_set_leq_epsilon1[f'psi_product({j}, {i}, {k})']['lhs'].add_variable('psi', _VariableIndexFormating.psi(j, i, k), 1)
                constraint_set_leq_epsilon1[f'psi_product({j}, {i}, {k})']['rhs'].add_variable('epsilon', _VariableIndexFormating.epsilon(j, i), 1)

                constraint_set_leq_epsilon2[f'psi_product({j}, {i}, {k})']['lhs'].add_variable('psi', _VariableIndexFormating.psi(j, i, k), 1)
                constraint_set_leq_epsilon2[f'psi_product({j}, {i}, {k})']['rhs'].add_variable('epsilon', _VariableIndexFormating.epsilon(j, k), 1)

                constraint_set_geq[f'psi_product({j}, {i}, {k})']['lhs'].add_variable('psi', _VariableIndexFormating.psi(j, i, k), 1)
                constraint_set_geq[f'psi_product({j}, {i}, {k})']['rhs'].add_variable('epsilon', _VariableIndexFormating.epsilon(j, i), 1)
                constraint_set_geq[f'psi_product({j}, {i}, {k})']['rhs'].add_variable('epsilon', _VariableIndexFormating.epsilon(j, k), 1)
                constraint_set_geq[f'psi_product({j}, {i}, {k})']['rhs'].add_constant(-1)

        return constraint_set_leq_epsilon1, constraint_set_leq_epsilon2, constraint_set_geq


