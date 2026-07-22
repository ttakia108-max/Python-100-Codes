# Finding LCM using GCD
num1 = int(input("Enter first prime number: "))
num2 = int(input("Enter second prime number: "))

# Finding GCD first
a, b = num1, num2

while b != 0:
    a, b = b, a % b

gcd = a
lcm = (num1 * num2) // gcd
print("The GCD of", num1, "and", num2, "is:", gcd)
print("The LCM of", num1, "and", num2, "is:", lcm)
print("The Product of", num1, "and", num2, "is:", num1 * num2)

if lcm == num1 * num2:
    print("LCM = Product. Hence proved.")
else:
    print("LCM != Product.")