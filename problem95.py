# Printing first 7 Factorial values
N = 7
fact = 1
print("First 7 Factorial values:")
for i in range(1, N + 1):
    fact *= i
    if i != N:
        print(fact, end=", ")
    else:
        print(fact)