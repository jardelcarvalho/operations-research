from lib import io
from lib import graph


if __name__ == '__main__':
    graph = graph.from_dataframe(
        io.load_data('test-cases/test1.csv'), 
        source_col='Source',
        sink_col='Sink',
        weight_col='Weight')

    print(graph)
    print()
    print(graph[0, 3])
    print(graph.nodes)
    print(graph.neighborhoods(1))
    print(graph.neighborhoods(4))
    print(graph.degree(1))
