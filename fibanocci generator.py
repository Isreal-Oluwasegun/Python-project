def fibonacci(n):
    a = b = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = a + b
            a =b
            b= n
            yield n

fibs = list(fibonacci(10))
print(fibs)

