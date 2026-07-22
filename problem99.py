# Printing Right-aligned Triangle Pattern
N = int(input("Enter height: "))
for i in range(1, N + 1):
    print(" " * (N - i) + "# " * i)