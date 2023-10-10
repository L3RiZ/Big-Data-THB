def fibonacci(n = 1): 
    result = []
    a = 0
    b = 1
    while n > 0:
        result.append(a) 
        c = a + b
        a = b
        b = c
        n -= 1
    return result

fibonacci10 = fibonacci(10)
a = fibonacci()
b = fibonacci(n = 6)
print(b)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]