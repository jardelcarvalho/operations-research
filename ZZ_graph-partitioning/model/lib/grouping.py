def intersection(a, b):
    if len(a) < len(b):
        return [e for e in a if e in b]
    else:
        return [e for e in b if e in a]

def create_components(edges):
    neighborhoods = {}
    for i, j in edges:
        if i not in neighborhoods:
            neighborhoods[i] = []
        if j not in neighborhoods:
            neighborhoods[j] = []
        neighborhoods[i].append(j)
        neighborhoods[j].append(i)
    
    components = []
    for i, j in edges:
        for k in intersection(neighborhoods[i], neighborhoods[j]):
            components.append((i, j, k))
        
    return components

def create_components_connections(components):
    pass

def select_edges(components, edges):
    pass

def generate_new_graph(nodes, edges):
    pass

def run(edges):
    components = create_components(edges)
    edges = create_components_connections(components)
    selected_edges = select_edges(components, edges)
    new_graph = generate_new_graph(components, selected_edges)
    return new_graph
