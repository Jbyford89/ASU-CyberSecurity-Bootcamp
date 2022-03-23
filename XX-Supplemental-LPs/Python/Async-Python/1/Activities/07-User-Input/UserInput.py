# input() function requests user input from the command line.
# The user's response is stored as the variable value.
name = input("What is your name? ")
# Notice the concatenation of the text and a variable
print("Hello " + name)

# User inputs are received as strings.
# They must be converted into integers or floats if we intend to do arithmetic.
number = input("Please enter a number to multiply by 2: ")
print(int(number) * 2)
