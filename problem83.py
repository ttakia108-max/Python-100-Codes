# Checking Strong Number
import math
num = 40585
temp = num
total_sum = 0

while temp > 0:
    digit = temp % 10
    total_sum += math.factorial(digit)
    temp = temp // 10

if total_sum == num:
    print(num, "is a Strong Number")
else:
    print(num, "is NOT a Strong Number")