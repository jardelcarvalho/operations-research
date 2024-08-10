import sys
sys.path.append('../../../utils')
sys.path.append('../')

import data_structures

import io
from lib import model


def _graph_from_dataframe(df, source_col, sink_col, weight_col):

    nodes = df[[source_col, sink_col]].to_numpy().ravel()
    edges = df[[source_col, sink_col]].to_numpy()
    weights = df[weight_col].to_numpy()

    return data_structures.Graph(nodes, edges, weights)

if __name__ == '__main__':
    graph = _graph_from_dataframe(
        io.load_data('../simple-test-cases/test3.csv'), 
        source_col='Source',
        sink_col='Sink',
        weight_col='Weight')

    model.initialize(graph, './lp.lp')

    model.run()
