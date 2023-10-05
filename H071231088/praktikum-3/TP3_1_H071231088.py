n = int(input(": "))

if n <= 0:
    print("Jumlah suku Fibonacci harus lebih dari 0")
elif n == 1:
    print("0")
else:
    a, b = 0, 1
    print("0 1", end=" ")
    for fib in range(2, n):
        fib = a + b
        print(fib, end=" ")
        a, b = b, fib

