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

#region variable indexation
...
#endregion variable indexation

#region model creation
_model = None

def _set_variables():
    pass

def _set_objective():
    pass

def _set_constraint1():
    pass

def _set_constraint2():
    pass

def _set_constraint3():
    pass

def _set_constraint4():
    pass

def _set_constraint5():
    pass

def _set_constraint6():
    pass

def _create_model():
    global _model

    _set_variables()
    _set_objective()
    _set_constraint1()
    _set_constraint2()
    _set_constraint3()
    _set_constraint4()
    _set_constraint5()
    _set_constraint6()
#endregion model creation

def initialize(graph, K, lp_file_path=None):
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