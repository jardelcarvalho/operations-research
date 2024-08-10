import sys
sys.path.append('../../utils')

import data_structures

from lib import io
from lib import model


def graph_from_dataframe(df, source_col, sink_col, weight_col):

    nodes = df[[source_col, sink_col]].to_numpy().ravel()
    edges = df[[source_col, sink_col]].to_numpy()
    weights = df[weight_col].to_numpy()

    return data_structures.Graph(nodes, edges, weights)

if __name__ == '__main__':
    graph = graph_from_dataframe(
        io.load_data('simple-tests/test5.csv'), 
        source_col='Source',
        sink_col='Sink',
        weight_col='Weight')

    model.initialize(graph, './lp.lp')
    model.run()
