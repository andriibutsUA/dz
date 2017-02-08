import random


def bubble_sort(lst):
    print('the original list is ', lst)
    the_range = len(lst)

    swapped = True
    while swapped:
        swapped = False
        for i in range(1, the_range):
            if lst[i - 1] > lst[i]:
                a = lst[i - 1]
                b = lst[i]
                print('swapping %d with %d' % (a, b))
                lst[i] = a
                lst[i - 1] = b
                print('the array is now ', my_list)
                swapped = True
    return lst


my_list = [random.randint(1,100) for x in range(10)]
print(bubble_sort(my_list))