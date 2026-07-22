# Checking Automorphic Number
num = int(input("Enter a number: "))
square = num * num

if str(square).endswith(str(num)):
    print(num, "is an Automorphic Number")
    print("Square =", square)
else:
    print(num, "is NOT an Automorphic Number")
    print("Square =", square)