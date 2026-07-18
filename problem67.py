# Sum of numbers divisible by 4 from 1 to 100
total = 0
for i in range(1, 101):
    if i % 4 == 0:
        total += i
print("Sum =", total)