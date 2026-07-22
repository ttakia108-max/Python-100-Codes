# Printing Lowercase Alphabet Triangle Pattern
N = int(input("Enter height: "))
for i in range(1, N + 1):
    for j in range(i):
        char = chr(97 + j)
        print(char, end=" ")
    print()