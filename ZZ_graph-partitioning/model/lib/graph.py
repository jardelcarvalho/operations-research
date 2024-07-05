import numpy as np

class _Graph:
    def __init__(self, nodes, edges, weights):
        nodes = np.unique(nodes)
        self.nodes_indices = {e: i for i, e in enumerate(nodes)}
        self.graph = np.zeros((len(nodes), len(nodes)), dtype=np.float64)
        self.__set_weights(edges, weights)

    def __set_weights(self, edges, weights):
        for (source, sink), weight in zip(edges, weights):
            self.graph[self.nodes_indices[source], self.nodes_indices[sink]] = weight


def from_dataframe(df, source_col, sink_col, weight_col):
    nodes = df[[source_col, sink_col]].to_numpy().ravel()
    edges = df[[source_col, sink_col]].to_numpy()
    weights = df[weight_col].to_numpy()

    return _Graph(nodes, edges, weights)

