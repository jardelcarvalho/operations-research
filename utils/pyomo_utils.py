import pyomo.environ as pyo

def set_variables_pyomo_model(model, all_variables_indices, within_map):
    for name in all_variables_indices:
        setattr(model, name, pyo.Var(all_variables_indices[name], within=within_map[name]))

def _evaluate_expression(model, expression_terms):
    variables = []
    for name in expression_terms.variables:
        var = getattr(model, name, None)
        for index, coef in expression_terms.variables[name]:
            variables.append(coef * var[index])
    return sum(variables) + sum(expression_terms.constants)

def set_constraints_pyomo_model(model, constraints_set_list):
    for name, constraints_set in constraints_set_list:
        constraint = pyo.Constraint(
            constraints_set.indices_names, 
            rule=lambda _, index: constraints_set.operation(
                _evaluate_expression(model, constraints_set.constraints[index]['lhs']), 
                _evaluate_expression(model, constraints_set.constraints[index]['rhs'])))

        setattr(model, name, constraint)

def set_objective_pyomo_model(model, expression_terms, sense):
    model.z = pyo.Objective(expr=_evaluate_expression(model, expression_terms), sense=sense)