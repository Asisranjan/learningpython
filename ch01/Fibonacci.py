def Fibonacci(n):
    a = 0
    b = 1
    while (a + b) < n:
        yield a
        future = a + b
        a = b
        b = future
    yield a
    yield b

for value in Fibonacci(10):
    print (value)

