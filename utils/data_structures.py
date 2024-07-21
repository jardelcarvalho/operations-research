import numpy as np

class Graph:
    def __init__(self, nodes, edges, weights=None):
        nodes = np.unique(nodes)
        if weights is None:
            weights = np.ones(len(edges), dtype=np.float64)
        else:
            weights = np.array(weights)

        self.__nodes_indices = {n: i for i, n in enumerate(nodes)}
        self.__indices_nodes = {i: n for i, n in enumerate(nodes)}
        self.__graph = np.zeros((len(nodes), len(nodes)), dtype=np.float64)
        self.__set_weights(edges, weights)
        
        self.__edges = [(*edges[i], weights[i]) for i in range(len(edges))]

    def __getitem__(self, i):
        source, sink = i
        return self.__graph[self.__nodes_indices[source], self.__nodes_indices[sink]]

    def __str__(self):
        return str(self.__graph)

    def __repr__(self):
        return str(self)

    def __set_weights(self, edges, weights):
        for (source, sink), weight in zip(edges, weights):
            self.__graph[self.__nodes_indices[source], self.__nodes_indices[sink]] = weight

    @property
    def nodes(self):
        return list(self.__nodes_indices.keys())

    @property
    def edges(self):
        return self.__edges

    @property
    def matrix(self):
        matrix = getattr(self, '__matrix', None)
        if matrix is None:
            matrix = np.zeros((len(self.nodes), len(self.nodes)), dtype=np.float64)
            for i, j, w in self.edges:
                matrix[self.__nodes_indices[i], self.__nodes_indices[j]] = w
                matrix[self.__nodes_indices[j], self.__nodes_indices[i]] = w
            setattr(self, '__matrix', matrix)
        return matrix

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

