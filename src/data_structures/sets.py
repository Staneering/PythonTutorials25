# Sets in Python

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)

# Removing elements
my_set.remove(3)  # Removes 3 from the set

# Sets do not allow duplicate values
my_set.add(4)  # Won't add 4 again

# Iterating over a set
for item in my_set:
    print(item)

# Checking membership
print("Is 5 in the set?", 5 in my_set)
