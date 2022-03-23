programmer_list = [
  {
    "name": "Jacob Deming",
    "age": 27,
    "fave_language": "Python",
    "skill_level": 80
  },{
    "name": "Billy Bob",
    "age": 30,
    "fave_language": "True Basic",
    "skill_level": 120
  },{
    "name": "Kelsey Queen",
    "age": 25,
    "fave_language": "C++",
    "skill_level": 83
  }
]

# Loop through the programmer_list one dictionary at a time
# The counter or index variable could be called anything
for programmer in programmer_list:
  # Picks an item from programmer_list
  # Loop through each dictionary's keys and associated values
  for key, value in programmer.items():
    # Print out the key and its value to the terminal
    print(key + ": " + str(value))

  # Add in a line between each new programmer in the list
  # Notice the indentation - this line is not part of nested loop
  print("---------")
