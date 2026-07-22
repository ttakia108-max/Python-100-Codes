# Average of odd series 1 + 3 + 5 + ... + N
N = int(input("Enter N: "))
total = 0
count = 0

for i in range(1, N + 1, 2):
    total += i
    count += 1
average = total / count
print("Average of odd series is:", average)