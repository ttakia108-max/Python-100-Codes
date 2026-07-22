# Finding length of a string without spaces
text = input("Enter a string: ")
count = 0
for char in text:
    if char != " ":
        count += 1
print("Length without spaces is:", count)