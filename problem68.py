# Print numbers divisible by 13 from 1 to N
n = int(input("Enter N: "))
for i in range(1, n + 1):
    if i % 13 == 0:
        print(i)