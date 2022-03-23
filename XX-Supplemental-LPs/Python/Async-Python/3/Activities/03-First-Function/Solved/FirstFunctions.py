# A large Python dictionary that will be used for the activity
# The key is an individual's name while the value is their SSN
large_dict = {
  "Tina Flemming": "619-16-7988",
  "Erica Shah": "164-51-7615",
  "Paula Ortiz": "051-83-3290",
  "James Hendricks": "776-83-2884",
  "Lauren King": "197-94-2398",
  "David Cowan": "252-92-1832",
  "Andrew Burton": "296-23-6842",
  "Julian Baker": "337-40-7543",
  "Scott Castro": "399-46-5595",
  "Billy Rodriguez": "014-18-2503",
  "Darrell Leblanc": "005-82-7918",
  "David Hammond": "561-17-6312"
}

# Defining a function called `printAllKeys()` that will print all of the keys in a dictionary one after another
def printAllKeys():

  # Create a loop that will navigate through `large_dict.keys()`
  for key in large_dict.keys():
    # Print out the current key and let the user know it is a name
    print("Name: " + key)

# Defining a function called `printAllValues()` that will print all of the values in a dictionary one after another
def printAllValues():

  # Create a loop that will navigate through `large_dict.values()`
  for value in large_dict.values():
    # Print out the current value and let the user know it is a SSN
    print("SSN: " + value)

# Defining a function called `printAllItems()` that will print all of the keys AND values in a dictionary one after another
def printAllItems():

  # Create a loop that will navigate through `large_dict.items()`
  for key,value in large_dict.items():
    # Print out the current items name and SSN one after another
    print("Name: " + key +  " || SSN: " + value)

# Calling the printAllKeys() function to run it
printAllKeys()
print("--------")

# Calling the printAllValues() function to run it
printAllValues()
print("--------")

# Calling the printAllItems() function to run it
printAllItems()