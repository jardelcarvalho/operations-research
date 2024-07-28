class ExpressionTerms:
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

class ConstraintsSet:
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

    @property
    def indices_names(self):
        return list(self.constraints.keys())

    def __getitem__(self, constraint_index):
        if constraint_index not in self.constraints:
            self.constraints[constraint_index] = {'rhs': ExpressionTerms(), 'lhs': ExpressionTerms()}
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