total_seconds = int(input("Enter total seconds: "))
minutes = total_seconds // 60
remaining_seconds = total_seconds % 60
print(total_seconds, "seconds is equal to:", minutes, "minutes and", 
remaining_seconds, "seconds")