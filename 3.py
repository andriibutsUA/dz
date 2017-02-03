def fib(n):
    a = 0
    b = 1
    for k in range(n):
        a, b = b, a + b

    return a


print(fib(6))