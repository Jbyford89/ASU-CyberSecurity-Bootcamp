# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit",
             "Swedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# Create an empty list to store all the candies selected
candyCart = []

# Print all the candies to the screen and their index in brackets
for candy in candyList:
    print("[" + str(candyList.index(candy)) + "] " + candy)

# Run through a loop which allows the user to choose which candies to buy
for x in range(allowance):
    selected = input("Which candy would you like to buy? ")

    # Add the candy at the index chosen to the candyCart list
    candyCart.append(candyList[int(selected)])

# Loop through the candyCart to print what candies were purchased
print("I brought...")
for candy in candyCart:
    print(candy)
