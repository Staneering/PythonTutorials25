# Lists in Python

# Creating a list
my_list = [1, 2, 3, "apple", True]

# Accessing elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Modifying a list
my_list.append(4)  # Add an item to the list
my_list[1] = "banana"  # Modify an item

# Iterating over a list
for item in my_list:
    print(item)

# Slicing a list
print("Sliced list:", my_list[1:4])  # From index 1 to 3
