# Create an empty dictionary, called inventory
inventory = {}

# Ask the user how many items they have in their inventory
# Convert to integer since input's value is a string
item_count = int(input("How many items do you have in your inventory? "))

# Use `range` and `for` to loop over each number up to the inventory number
for x in range(item_count):

    # Prompt the user for the name of an item in their inventory ("What's the item? ")
    item_name = input("What's the item? ")

    # Prompt the user for the price of that item ("How much does it cost? ")
    item_price = input("What's its price? ")

    # Put the item into the dictionary as the key, and associate it with its price
    inventory[item_name] = float(item_price)

    # Creating separation between each new item prompt
    print("--------")

# Use `items` to loop through the dictionary and print the info to the screen
for item, price in inventory.items():
    print("The price of " + item + " is $" + str(price))

    # Check if the price of the item is less than five
    if (price < 5):

        # If the price is less than five, print out "This item is on sale!"
        print("This item is on sale!")

    # Creating separation between each item
    print("--------")
