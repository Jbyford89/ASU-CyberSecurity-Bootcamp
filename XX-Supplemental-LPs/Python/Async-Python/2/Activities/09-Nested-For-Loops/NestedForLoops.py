# A list of five letters
letter_list = ["B", "I", "N", "G", "O"]
# A list of 20 numbers
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# The first loop moves through all the letters in the letter list
for letter in letter_list:

  # The second loop moves through all the numbers in the number list
  for number in numbers_list:

    # Print out the unique letter/number combination
    print(letter + str(number))

# Dictionary of highly sensitive personal information
my_nemesis = {
    "Weakness": "Kryptonite",
    "Greatest Fear": "Spiders",
    "Secret Lair": "300 Nemesis Drive #665"
}

# The dictionary.keys() function places all of the keys of a dictionary into a list
key_list = my_nemesis.keys()
print("I have dirt on my nemesis's...")
for key in key_list:
  print(key)

# Use dictionay.values() to get a list of all the secret information
value_list = my_nemesis.values()
print("To ruin my rival's life, you need to know about...")
for value in value_list:
  print(value)

# Use dictionary.items() to get each key/value pair in a loop
for item, juicy_tidbit in my_nemesis.items():
    print("My nemesis's " + item + " is " + juicy_tidbit + ".")
