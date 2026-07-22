# Checking Neon Number
num = 1
square = num * num
temp = square
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp = temp // 10

if sum_digits == num:
    print(num, "is a Neon Number")
    print("Square =", square)
else:
    print(num, "is NOT a Neon Number")
    print("Square =", square)