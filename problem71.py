# Sum of digits using string conversion
num = input("Enter a number: ")
sum = 0
for digit in num:
    sum += int(digit)
print("Sum of digits =", sum)