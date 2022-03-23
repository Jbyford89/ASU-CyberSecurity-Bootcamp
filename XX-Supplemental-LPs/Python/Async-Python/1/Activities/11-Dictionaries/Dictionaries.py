# Unlike lists, dictionaries store information in pairs
# ---------------------------------------------------------------
# A list of actors' names
actor_names = [
    "Denzel Washington",
    "Gary Oldman",
    "Mila Kunis",
    "Jennifer Beals"
]

# A dictionary of actors
actors = {
    "protagonist": "Denzel Washington",
    "antagonist"	: "Gary Oldman",
    "deuteragonist": "Mila Kunis",
    "love interest": "Jennifer Beals",
}
print(actors["deuteragonist"])

# ---------------------------------------------------------------

# A dictionary can contain multiple pairs of information
actress = {
    "name": "Angelina Jolie",
    "genre": "Action",
    "nationality": "United States"
}

# ---------------------------------------------------------------

# A dictionary can contain multiple types of information
# Here we have a list as a dictionary value. Remember lists can't be dictionary keys but they can be values
stallone = {
    "name": "Sylvester Stallone",
    "age": 73,
    "married": True,
    "best movies": [
        "Rocky",
        "Rocky 2",
        "Rocky 3"
    ],
}

# Notice the concatenation
print(stallone["name"] + " was in " + stallone["best movies"][0] + ".")
print(stallone["name"] + " is " + str(stallone["age"]) + " years old.")
# ---------------------------------------------------------------

# A dictionary can even contain another dictionary
film = {
    "title": "Interstellar",
    "revenues": {
        "United States": "$360 milliion",
        "China": "$250 million",
        "United Kingdom": "$73 million",
    },
}

print(film["title"] + " made " + film["revenues"]
      ["United States"] + " in the US.")
# ---------------------------------------------------------------
