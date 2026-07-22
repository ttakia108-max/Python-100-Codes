# Average of even square series 2^2 + 4^2 + ... + 100^2
total = 0
count = 0

for i in range(2, 101, 2):
    total += i ** 2
    count += 1

average = total / count

print("Average of even square series is:", average)