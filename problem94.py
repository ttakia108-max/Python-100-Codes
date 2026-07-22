# Store first N Fibonacci numbers in a list
N = int(input("Enter number of terms (N): "))
fib = []
a, b = 0, 1

for i in range(N):
    fib.append(a)
    a, b = b, a + b

print("Fibonacci numbers are:", fib)