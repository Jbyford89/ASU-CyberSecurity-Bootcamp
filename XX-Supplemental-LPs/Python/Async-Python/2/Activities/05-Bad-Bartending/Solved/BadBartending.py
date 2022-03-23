# Set a variable, called `drinking_age`, to 21
drinking_age = 21
# Prompt the user for their age
user_age = int(input("How old are you? "))

# Check if the user is 21 or older
if user_age >= 21:
    # If so, create a list, called `drinks`. Store four cocktails in it.
    drinks = ["Mai Tai", "Dark and Stormy", "Minotauro", "Old Fashioned"]
    
    # Prompt the user for the drink they want to order
    user_drink = input("What's your order? ")
    
    # Check if the user's selection is in `drinks`
    if user_drink in drinks:
        # If so, print: `"Cheers!"`
        print("Cheers!")
    else:
        # Print: `"I don't know that one..."
        print("I don't know that one...")


else:
    # If not, print: "Your fake ID looks really fake."
    print("Your fake ID looks really fake.")
