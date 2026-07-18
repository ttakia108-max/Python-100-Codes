# Print numbers divisible by 3 or 5 from 1 to N
n = int(input("Enter N: "))
for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i)