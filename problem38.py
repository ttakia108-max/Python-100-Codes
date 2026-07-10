import math
radius = float(input("Enter radius of cylinder: "))
height = float(input("Enter height of cylinder: "))
volume = math.pi * (radius ** 2) * height
print("The volume of cylinder is:", round(volume, 2))