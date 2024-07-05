import numpy as np

class _Graph:
    def __init__(self, nodes, edges, weights=None):
        nodes = np.unique(nodes)
        if weights is None:
            weights = np.ones(len(edges), dtype=np.float64)

        self.__nodes_indices = {n: i for i, n in enumerate(nodes)}
        self.__indices_nodes = {i: n for i, n in enumerate(nodes)}
        self.__graph = np.zeros((len(nodes), len(nodes)), dtype=np.float64)
        self.__set_weights(edges, weights)
        
        self.__edges = edges
        self.__edges_weights = np.concatenate([edges, weights[..., np.newaxis]], axis=-1)

    def __getitem__(self, i):
        source, sink = i
        return self.__graph[self.__nodes_indices[source], self.__nodes_indices[sink]]

    def __str__(self):
        return str(self.__graph)

    def __repr__(self):
        return str(self)

    @property
    def nodes(self):
        return list(self.__nodes_indices.keys())

    @property
    def edges(self):
        return self.__edges

    @property
    def edges_weights(self):
        return self.__edges_weights

    def __set_weights(self, edges, weights):
        for (source, sink), weight in zip(edges, weights):
            self.__graph[self.__nodes_indices[source], self.__nodes_indices[sink]] = weight

    def neighborhoods(self, n):
        neighborhoods = [
            self.__indices_nodes[i]
            for i, weight in enumerate(self.__graph[self.__nodes_indices[n]]) 
            if weight != 0]
        return neighborhoods

    def degree(self, n):
        return len(self.neighborhoods(n))

def from_dataframe(df, source_col, sink_col, weight_col):

    nodes = df[[source_col, sink_col]].to_numpy().ravel()
    edges = df[[source_col, sink_col]].to_numpy()
    weights = df[weight_col].to_numpy()

    return _Graph(nodes, edges, weights)

