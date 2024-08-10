from lib import data
from lib.decomposition import VariableIndexFormating, DecomposedModelStructure

import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../../utils'))

import expressions_decomposition
import pyomo_utils

import pyomo.environ as pyo
import numpy as np

_SOLVER_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../../solvers/Cbc/bin/cbc.exe')

_MODEL = None

def initialize(graph, lp_file_path=None):
    global _MODEL

    data.initialize(graph)

    objective = DecomposedModelStructure.objective()
    c4_leq1, c4_leq2, c4_geq = DecomposedModelStructure.c4_rho_linearization()
    constraints_set_list = [
        ('mutal_neighborhoods', DecomposedModelStructure.c1()),
        ('mutual_neighborhoods_integrity_lhs', DecomposedModelStructure.c2()),
        ('mutual_neighborhoods_integrity_rhs', DecomposedModelStructure.c3()),
        ('rho_linearization_leq1', c4_leq1),
        ('rho_linearization_leq2', c4_leq2),
        ('rho_linearization_geq', c4_geq)]

    all_variables_indices = expressions_decomposition.get_grouped_variables_indices(
        objective, [c for _, c in constraints_set_list])

    model = pyo.ConcreteModel()

    within_map = {name: pyo.Binary for name in all_variables_indices}

    pyomo_utils.set_variables_pyomo_model(model, all_variables_indices, within_map)
    pyomo_utils.set_constraints_pyomo_model(model, constraints_set_list)
    pyomo_utils.set_objective_pyomo_model(model, objective, pyo.minimize)

    if lp_file_path is not None:
        model.write(lp_file_path, io_options={'symbolic_solver_labels': True})

    _MODEL = model

def run():
    solver = pyo.SolverFactory('cbc', executable=_SOLVER_PATH)
    solver.options['LogFile'] = 'log.log'

    status = solver.solve(_MODEL, options={"threads": 1})

    print(status)

    print(f'\n\n### OBJECTIVE: {_MODEL.z()}')

    active_edges = []

    print('\n### DEACTIVATED EDGES')
    count = 0
    for i, j, w in data.DATA['graph'].edges:
        index = VariableIndexFormating.x(i, j)
        if _MODEL.x[index].value != 1:
            print(index, _MODEL.x[index].value)
            count += 1
        else:
            active_edges.append((i, j, w))

    print('\nTotal deactivated edges:', count)

    return active_edges

