# Initial variable to track game play
user_play = "y"

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_number = input("How many numbers? ")

    # Loop through the numbers. (Be sure to make the string into an integer.)
    # Remember, the value of input is of string type
    # So, we need to convert it to an integer before comparing with the value of x
    for x in range(int(user_number)):

        # Print each number in the range
        print(x)

    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")
