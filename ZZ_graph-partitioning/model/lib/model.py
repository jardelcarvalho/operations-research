from lib import data
from lib.decomposition import DecomposedModelStructure

import sys
sys.path.append('../../utils')
import expressions_decomposition

import pyomo.environ as pyo
import numpy as np


def _create_variables_pyomo_model(model, all_variables_indices, within_map):
    for name in all_variables_indices:
        setattr(model, name, pyo.Var(all_variables_indices[name], within=within_map[name]))

def _evaluate_expression(model, expression_terms):
    variables = []
    for name in expression_terms.variables:
        var = getattr(model, name, None)
        for index, coef in expression_terms.variables[name]:
            variables.append(coef * var[index])
    return sum(variables) + sum(expression_terms.constants)

def _create_constraints_pyomo_model(model, constraints_set_list):
    for name, constraints_set in constraints_set_list:
        constraint = pyo.Constraint(
            constraints_set.indices_names, 
            rule=lambda _, index: constraints_set.operation(
                _evaluate_expression(model, constraints_set.constraints[index]['lhs']), 
                _evaluate_expression(model, constraints_set.constraints[index]['rhs'])))

        setattr(model, name, constraint)

def _create_objective_pyomo_model(model, expression_terms, sense):
    model.z = pyo.Objective(expr=_evaluate_expression(model, expression_terms), sense=sense)

_MODEL = None

def initialize(graph, Pi, lp_file_path=None):
    global _MODEL

    data.initialize(graph, Pi)

    objective = DecomposedModelStructure.objective()
    c9_leq1, c9_leq2, c9_geq = DecomposedModelStructure.c9_xi_linearization()
    c10_leq1, c10_leq2, c10_geq = DecomposedModelStructure.c10_psi_linearization()
    constraints_set_list = [
        ('node_can_represent_unique_partition', DecomposedModelStructure.c1()),
        ('partition_can_have_unique_representant', DecomposedModelStructure.c2()),
        ('relaxation_of_number_of_partitions', DecomposedModelStructure.c3()),
        ('maximum_relaxation_of_partitions', DecomposedModelStructure.c4()),
        ('representants_cannot_be_adjacent', DecomposedModelStructure.c5()),
        ('mutal_neighborhoods', DecomposedModelStructure.c6()),
        ('mutual_neighborhoods_integrity_lhs', DecomposedModelStructure.c7()),
        ('mutual_neighborhoods_integrity_rhs', DecomposedModelStructure.c8()),
        ('xi_linearization_leq1', c9_leq1),
        ('xi_linearization_leq2', c9_leq2),
        ('xi_linearization_geq', c9_geq),
        ('psi_linearization_leq1', c10_leq1),
        ('psi_linearization_leq2', c10_leq2),
        ('psi_linearization_geq', c10_geq)]

    all_variables_indices = expressions_decomposition.get_grouped_variables_indices(
        objective, [c for _, c in constraints_set_list])

    # for name in all_variables_indices:
    #     print(f'{name}:\t', '  '.join(all_variables_indices[name]), sep='', end='\n\n')

    model = pyo.ConcreteModel()

    within_map = {name: pyo.Binary for name in all_variables_indices}
    within_map['kappa'] = pyo.PositiveReals

    _create_variables_pyomo_model(model, all_variables_indices, within_map)
    _create_constraints_pyomo_model(model, constraints_set_list)
    _create_objective_pyomo_model(model, objective, pyo.minimize)

    if lp_file_path is not None:
        model.write(lp_file_path, io_options={'symbolic_solver_labels': True})

    _MODEL = model

def run():
    solver = pyo.SolverFactory('cbc', executable='../../solvers/Cbc/bin/cbc.exe')
    solver.options['LogFile'] = 'log.log'

    status = solver.solve(_MODEL, options={"threads": 8})

    print(status)

    print(f'\n\n### OBJECTIVE: {_MODEL.z()}')

    print('\n### PARTITIONS SLACK')
    for index in _MODEL.kappa:
        print(index, _MODEL.kappa[index].value)

    print('\n### PARTITIONS REPRESENTANTS')
    for index in _MODEL.rho:
        if _MODEL.rho[index].value != 0:
            print(index, _MODEL.rho[index].value)

    print('\n### DEACTIVATED EDGES')
    for index in _MODEL.epsilon:
        if _MODEL.epsilon[index].value != 1:
            print(index, _MODEL.epsilon[index].value)