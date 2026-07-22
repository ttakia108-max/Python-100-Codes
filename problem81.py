# Checking Perfect Number (496)
num = 496
sum_divisors = 0

for i in range(1, (num // 2) + 1):
    if num % i == 0:
        sum_divisors += i

if sum_divisors == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is NOT a Perfect Number")