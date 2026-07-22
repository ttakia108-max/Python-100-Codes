# Printing a Number Square Pattern
N = int(input("Enter size of square: "))
for i in range(N):
    for j in range(1, N + 1):
        print(j, end=" ")
    print()