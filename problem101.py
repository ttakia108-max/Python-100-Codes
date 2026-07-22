# Printing a Number Pyramid
N = int(input("Enter height of pyramid: "))
for i in range(1, N + 1):
    print(" " * (N - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()