import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../utils'))
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import os

import data_structures

from lib import model


def optimize(edges):
    graph_nodes, graph_edges, edges_weights = set(), [], []
    for i, j, w in edges:
        graph_nodes.add(i)
        graph_nodes.add(j)
        edges_weights.append(w)
        graph_edges.append((i, j))
    graph_nodes = list(graph_nodes)
    
    graph = data_structures.Graph(graph_nodes, graph_edges, edges_weights)

    model.initialize(graph, None)

    active_edges = model.run()

    return active_edges