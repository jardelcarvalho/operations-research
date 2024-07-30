def create_components(edges):
    pass

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
