def key_x2(dictionary):
    lst = []
    for key in dictionary:
        lst.append(dictionary[key] * 2)
    return lst

print(key_x2({'a': 1, 'b': 2, 'c': 3, 'd': 4}))
