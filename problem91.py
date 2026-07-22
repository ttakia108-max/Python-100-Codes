# Sum of cube series 1^3 + 2^3 + ... + 10
total = 0
for i in range(1, 11):
    total += i ** 3
print("Sum of cube series is:", total)