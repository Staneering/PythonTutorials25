# Dictionaries in Python

# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing values by key
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])

# Adding a new key-value pair
my_dict["job"] = "Engineer"

# Iterating through the dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Using get() to avoid KeyError
print("Country:", my_dict.get("country", "Not found"))  # "Not found" is the default value if the key doesn't exist
