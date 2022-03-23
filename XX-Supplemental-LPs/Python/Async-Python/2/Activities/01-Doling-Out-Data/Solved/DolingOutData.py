
# Declare a variable called `name`, and store your name inside it.
name = "Peleke"

# Print the message: "My name is <Your name here>"
print("My name is " + name + ".")

# Declare a variable called `age`, and store your age inside it.
age = 42

# Print the message: "I am <Your age here> years old."
print("I am " + str(age) + " years old.")

#######################################################
# Declare a variable called `pizza_price`, and store a number inside it.
pizza_price = 12

# Declare a variable called `number_of_pizzas`, and store a number inside it.
number_of_pizzas = 4

# Store the total price for all the pizzas in a variable called `total_price_of_pizzas`.
total_price = number_of_pizzas * pizza_price

# Print the message: "The price of a single pizza is $<Price of pizza>."
print("The price of a single pizza is $" + str(pizza_price) + ".")

# Print the message: "We are buying <Number of pizzas> pizzas."
print("We are buying " + str(number_of_pizzas) + " pizzas.")

# Print the message: "The total price for all the pizzas is <Total price of pizzas>."
print("The total price of pizza is $" + str(total_price) + ".")

#######################################################
# Create a list called `favorite_countries`. Store the name of four countries inside it.
favorite_countries = ["Norway", "Spain", "Taiwan", "Morocco"]

# Print the message: "My favorite countries are: <Your list here>."
print("My favorite countries are: " + str(favorite_countries) + ".")

#######################################################
# Create a dictionary called `contact_information` and store a home phone number, a cellphone number, and an email address inside of it.
contact_information = {
    "email": "BoBoTheClown@gmail.com",
    "cell_number": "203-976-0988",
    "home_phone": "203-867-5309"
}

# Print out the message: "Please contact me at <Email> or call me at <Home phone>"
print("Please contact me at " +
      contact_information["email"] + " or call me at " + contact_information["home_phone"])

# Print out the message: "In case of an emergency call <Cell number>"
print("In case of an emergency, call " + contact_information["cell_number"])
