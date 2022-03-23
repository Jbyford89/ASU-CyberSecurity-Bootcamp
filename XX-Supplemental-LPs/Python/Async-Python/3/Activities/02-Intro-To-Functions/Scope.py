
# This variable is defined at the top level of the application
# This means that its scope is "global" and it can be referenced anywhere
global_variable = "I can go anywhere!"

# Creating a function
def printPhrases():

  # This variable is defined within a function
  # This means that it can only be referenced within this function
   local_variable = "I only exist in this function!"

  # Printing out the two phrases to the console
   print(global_variable)
   print(local_variable)

# Calling the function to run the code it contains
printPhrases()

print("----------")

# Printing `global_variable` still works since it exists across the entire application
print(global_variable)

# Trying to print `local_variable` outside of the function returns an error
print(local_variable)

