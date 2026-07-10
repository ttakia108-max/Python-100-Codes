
age = int(input("Enter your age: "))
has_id = input("Do you have ID card? (yes/no): ") == "yes"
can_enter = (age >= 18) and has_id
print("Can enter restricted area (age >= 18 AND has ID):", can_enter)
discount = (age < 12) or (age > 60)
print("Eligible for special discount (age < 12 OR age > 60):", discount)
print("Is NOT eligible for discount:", not discount)