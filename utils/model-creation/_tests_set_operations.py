import set_operations

print(set_operations.recursive_unpacking([1, 2, 3, 4, 5]))
print(set_operations.recursive_unpacking([1, 2, 3, 4, 5, (6, 7), ((8, 9), 10), {(11, (12, 13))}]))
print(set_operations.recursive_unpacking([]))
print()
print(set_operations.product([[1, 2, 3], [4, 5], [3]]))
print(set_operations.product([[1, 2, 3], [4, 5]], unpack=True))
print()
print(set_operations.intersection([[1, 2, 3], [4, 5]]))
print(set_operations.intersection([[1, 2, 3], [1, 3]]))
print(set_operations.intersection([[1, 2, (2, 3)], [(2, 3), 1, 3]]))
print(set_operations.intersection([[1, 2, (2, 3)], [(2, 3), 1, 3]], unpack=True))
print(set_operations.intersection([[1, 2, 3], [2]]))
print(set_operations.intersection([[1, 2, 3], []]))
print(set_operations.intersection([[1, 2, 3]])) #Must raise AssertionError