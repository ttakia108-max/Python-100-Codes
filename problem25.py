list1 = [10, 20, 30]
list2 = [10, 20, 30]
list3 = list1 
print("list1 == list2 (Same values?):", list1 == list2)
print("list1 is list2 (Same memory object?):", list1 is list2)
print("list1 is list3 (Same memory object?):", list1 is list3)
print("Memory ID of list1:", id(list1))
print("Memory ID of list2:", id(list2))
print("Memory ID of list3:", id(list3))