import sys
sys.path.append('../')

import data_structures

G = data_structures.Graph([1, 2, 3, 4, 5], [(1, 2), (1, 3), (2, 3), (1, 4), (4, 5)], [1.2, 2, 3, 2.5, 1])
print(G.nodes)
print(G.edges)
print(G.matrix)
print()
print(G.neighborhoods(1))