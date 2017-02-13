def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result += 1/n
            print(str(1) + '/' + str(i))
        return result

print(harmonic_sum(5))