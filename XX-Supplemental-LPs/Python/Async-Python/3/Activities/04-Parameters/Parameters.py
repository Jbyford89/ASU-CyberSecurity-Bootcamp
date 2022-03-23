
# Defining a function and giving it the parameter of "name"
# "name" is a temporary variable that only exists within the scope of this function
def printName(name):
  print("Oh! Hello " + name)

# Now any string value can be passed into the function within the parentheses
printName("Mark")
printName("Rose")
printName("Denny")

# Functions can be given multiple parameters
# Parameters can also be provided with default values
def recordScore(name, score=0):
  # The score that is printed out will default to 0 if none is provided
  # First value
  print(name + "'s score is " + str(score))

recordScore("Jacob")
recordScore("Ahmed", 20)
recordScore("Steven", 15)

