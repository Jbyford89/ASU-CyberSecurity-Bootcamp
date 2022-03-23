# Create a list and save it to a variable
hobbies = ["Rock Climbing", "Bug Collecting", "Cooking", "Knitting", "Writing"]
print(hobbies)

# Select the first, second and fifth values from the list
print(hobbies[0])
print(hobbies[1])
print(hobbies[4])

# len() tells us how long the list is (5)
print(len(hobbies))

# Use index() to find the index of a specific value in a list
print(hobbies.index("Cooking"))

# Use append() to add values to the end of the list
hobbies.append("Gaming")
print(hobbies)

# Use remove() to remove values from the list
hobbies.remove("Bug Collecting")
print(hobbies)

