#Print multiples of 5 from 1 to N
n = int(input("Enter the value of N: "))

for num in range(1, n + 1):
    if num % 5 == 0:
        print(num)