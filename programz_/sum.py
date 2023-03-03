def power(m, n):
    result = 1
    for i in range((n)):
        result *= m
    return result


m = 2
n = 2
result = power(m, n)
print(result) 