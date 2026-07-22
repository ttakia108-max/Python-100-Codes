# Sum of series 5^2 + 10^2 + ... + 100^2
total = 0
for i in range(5, 101, 5):
    total += i ** 2
print("Sum of the series 5^2 + ... + 100^2 is:", total)