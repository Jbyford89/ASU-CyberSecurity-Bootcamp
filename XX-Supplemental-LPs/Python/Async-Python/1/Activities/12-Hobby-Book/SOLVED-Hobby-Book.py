# Dictionary full of info
my_info = {
    "name": "Jack",
    "occupation": "coder",
    "age": 21,
    "hobbies": [
        "coding",
        "eating",
        "sleeping",
        "gaming"
    ],
    "wake-up": {
        "Mon": 10,
        "Friday": 10,
        "Saturday": 1,
        "Sunday": 1,
    },
}

# Print out results stored in the dictionary
print("Hello I am " + my_info["name"] +
      " and I am a " + my_info["occupation"] + ".")
print("I have " + str(len(my_info["hobbies"])) + " hobbies!")
print("One of my hobbies is " + my_info["hobbies"][2] + ".")
print("On the weekend I get up at " +
      str(my_info["wake-up"]["Saturday"]) + ".")
