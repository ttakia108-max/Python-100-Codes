chocolates = int(input("Enter total chocolates: "))
children = int(input("Enter number of children: "))
per_child = chocolates // children
remaining = chocolates % children
print("Each child gets:", per_child, "chocolates")
print("Chocolates left:", remaining)