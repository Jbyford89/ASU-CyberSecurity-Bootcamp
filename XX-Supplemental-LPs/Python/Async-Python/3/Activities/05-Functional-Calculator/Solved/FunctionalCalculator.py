# The `addition()` function takes in two integers and adds them together
def addition(x,y):
  outcome = x+y
  print(str(x) + "+" + str(y) + "=" + str(outcome))

# The `subtraction()` function takes in two integers and subtracts one from the other
def subtraction(x,y):
  outcome = x-y
  print(str(x) + "-" + str(y) + "=" + str(outcome))

# The `multiplication()` function takes in two integers and multiplies them together
def multiplication(x,y):
  outcome = x*y
  print(str(x) + "*" + str(y) + "=" + str(outcome))

# The `division()` function takes in two integers and divides one by the other
def division(x,y):
  outcome = x/y
  print(str(x) + "/" + str(y) + "=" + str(outcome))

# Set a default value for a variable to use for the while loop
# When the value of go_again is set to anything but "y", the while loop will stop
go_again = "y"

while str(go_again) == "y":
    # Ask the user what kind of calculation they want to perform
    userChoice = int(input("What kind of calculation would you like to perform?\n[1]Addition\n[2]Subtraction\n[3]Multiplication\n[4]Division\nEnter Choice: "))
    print("-------------------------")

    # Conditional tree to determine which function will run based upon the user's choice
    if(userChoice == 1):
        # Collect and store two numbers from the user
        firstNumber = int(input("What is the first number? "))
        secondNumber = int(input("What is the second number? "))

        # Call the addition function
        addition(firstNumber, secondNumber)
    elif(userChoice == 2):
        # Collect and store two numbers from the user
        firstNumber = int(input("What is the first number? "))
        secondNumber = int(input("What is the second number? "))

        # Call the subtraction function
        subtraction(firstNumber, secondNumber)
    elif(userChoice == 3):
        # Collect and store two numbers from the user
        firstNumber = int(input("What is the first number? "))
        secondNumber = int(input("What is the second number? "))

        # Call the multiplication function
        multiplication(firstNumber, secondNumber)
    elif(userChoice == 4):
        # Collect and store two numbers from the user
        firstNumber = int(input("What is the first number? "))
        secondNumber = int(input("What is the second number? "))

        # Call the division function
        division(firstNumber, secondNumber)
    else:
        print("Not a specified option")

    go_again = input("Should we go again? (y)es or (no) >> ")

print("Thank you for playing!")
