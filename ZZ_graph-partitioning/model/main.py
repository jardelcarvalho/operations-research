from lib import io
from lib import graph
from lib import lp_model


if __name__ == '__main__':
    k = 2
    graph = graph.from_dataframe(
        io.load_data('test-cases/test1.csv'), 
        source_col='Source',
        sink_col='Sink',
        weight_col='Weight')

    lp_model.initialize(graph, k)

    print(graph)
    # print()
    # print(graph[1, 3])
    # print(graph.nodes)
    # print(graph.neighborhoods(1))
    # print(graph.neighborhoods(4))
    # print(graph.degree(1))
    lp_model.run()
