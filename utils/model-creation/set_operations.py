def _validate_args(arrays, unpack):
    assert len(arrays) > 1, 'Set operations needs at least two operands'
    assert isinstance(unpack, bool), 'Invalid unpack argument'

def _format_result(result, unpack):
    if unpack:
        result = recursive_unpacking(result)
    return set(result)

def recursive_unpacking(element):
    if not isinstance(element, (tuple, list, set)):
        return [element]
    result = []
    for entry in element:
        result += recursive_unpacking(entry)
    return result

def product(arrays, unpack=False):
    _validate_args(arrays, unpack)
    current = []
    for i in range(len(arrays)):
        temp = []
        if len(current) > 0:
            for a in current:
                for b in arrays[i]:
                    temp.append((a, b))
        else:
            temp = [e for e in arrays[i]]
        current = temp
    return _format_result(current, unpack)

def intersection(arrays, unpack=False):
    _validate_args(arrays, unpack)
    idx, smalest_array, _ = min(
        map(lambda enum: (*enum, len(enum[1])), enumerate(arrays)), 
        key=lambda t: t[2])
    current = [element for element in smalest_array]
    for i, other in enumerate(arrays):
        if i != idx:
            temp = []
            for element in other:
                if element in current:
                    temp.append(element)
            current = temp
    return _format_result(current, unpack)
