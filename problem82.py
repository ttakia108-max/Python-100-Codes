# Printing all Armstrong Numbers from 1 to 1000
for num in range(1, 1001):
    num_str = str(num)
    power = len(num_str)
    total_sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total_sum += digit ** power
        temp = temp // 10

    if total_sum == num:
        print(num)