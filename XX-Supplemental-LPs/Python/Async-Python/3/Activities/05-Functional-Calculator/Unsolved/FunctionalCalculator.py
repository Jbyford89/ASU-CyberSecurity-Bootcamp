# The `addition()` function takes in two integers, adds them together, and prints out the operation
def addition(x, y):
    outcome = x+y
    print(str(x) + "+" + str(y) + "=" + str(outcome))

# The `subtraction()` function takes in two integers, subtracts one from the other, and prints out the operation


# The `multiplication()` function takes in two integers, multiplies them together, and prints out the operation


# The `division()` function takes in two integers, divides one by the other, and prints out the operation

go_again = "y"

# Everything from here to the end should be in a while loop that checks if the user wants to play again

# Ask the user what kind of calculation they want to perform
userChoice = int(input(
    "What kind of calculation would you like to perform?\n[1]Addition\n[2]Subtraction\n[3]Multiplication\n[4]Division\nEnter Choice: "))
print("-------------------------")
# Conditional tree to determine which function will run based upon the user's choice
if(userChoice == 1):

    # Collect and store two numbers from the user
    firstNumber = int(input("What is the first number? "))
    secondNumber = int(input("What is the second number? "))

    # Call the addition function
    addition(firstNumber, secondNumber)

# If user choice is 2
elif(userChoice == 2):

    # Collect and store two numbers from the user

    # Call the subtraction function

    # If user choice is 3
elif(userChoice == 3):

    # Collect and store two numbers from the user

    # Call the multiplication function

    # If user choice is 4
elif(userChoice == 4):

    # Collect and store two numbers from the user

    # Call the division function

    # Else print out "Not a specified option"
else:
print("Not a specified option")

# Ask the user if they'd like to play again. If yes, go back to asking what kind of calcuclation they'd like to perform. If no, exit with a message that says "Thank you for playing!"
