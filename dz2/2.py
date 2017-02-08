def product(l1, l2):
    product_list = []
    for i in range(len(l1)):
        product_list.append(l1[i] * l2[i])
    return product_list

print(product([1, 8, 2, 3], [1, 9, 2, 4]))
