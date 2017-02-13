def print_z(width):
    print('* ' * width)
    x = width * 2 - 3
    while x > 0:
        print(' ' * (x - 1), '*')
        x -= 1
    print('* ' * width)
    return ''


print(print_z(4))
