x = 1
y = 10

# Checks that both conditions are met using "and"
if (x == 1 and y == 10):
  print("Both values returned true")

# Checks if either of two conditions are met using "or"
if (x < 45 or y < 5):
  print("One or more of the statements were true")

# If - Elif - Else
# The elif statement will run when the if statement returns as false but its own condition returns as true
# The else statement will run when both the if and elif conditions return as false
if (y < 5):
  print("y is less than 5")
elif (y == 5):
  print("y is equal to 5")
else:
  print("y is greater than 5")

# Nested if statements allow for more specific conditional pathways
if (x < 10):
  # We only get here if the value of x is less than 10
  if (y < 5):
      print("x is less than 10 and y is less than 5")
  elif (y == 5):
    # We only get here if the value of x is less than 10 AND
    # the value of y is not less than 5
      print("x is less than 10 and y is equal to 5")
  else:
    # If x is less than 10 but none of the nested conditionals are true
      print("x is less than 10 and y is greater than 5")

# Note that there was no else statement if (x<10)
# So if the first condition is false/not true, we skip over the rest

# Checking whether a value is inside of a list using the `in` keyword
if (x in [1,2,3,4,5,6,7]):
  print("The value of x was inside of the list")
else:
  print("The value of x was not inside of the list")
