def dic(keys, value):
    """
    Функция, создаёт словарь из ключей и значений из списков разной длины.
    Если ключу не хватило значения, то значение будет None.
    Значения, которым не хватило ключей будут игноририроваться.
    """

    d = dict.fromkeys(keys, None)

    for i, k in enumerate(keys):
        if i < len(value):
            d.update({k: value[i]})
        else:
            break

    return d


print('\n', dic([1, 2, 3, 4, 5], ['h', 'e', 'l', 'l', 'o']))  # {1:'h', 2:'e', 3:'l', 4:'l', 6:'o'}
print('\n', dic(['M', 'a', 'y'], ['J', 'u', 'n', 'e']))  # {'M':'J', 'a':'u', 'y':'n'}

assert (dic([], []) == {})
assert (dic([0, 1], []) == {0: None, 1: None})
assert (dic([], [1, 2]) == {})
assert (dic([3, 4, 5], ['a', 'b', ]) == {3: 'a', 4: 'b', 5: None})
assert (dic([6, 7], ['c', 'd', 'e']) == {6: 'c', 7: 'd'})
