# Check if two numbers are Co-prime using Euclidean Algorithm
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
a, b = num1, num2

while b != 0:
    a, b = b, a % b

if a == 1:
    print(num1, "and", num2, "are Co-prime.")
else:
    print(num1, "and", num2, "are NOT Co-prime.")