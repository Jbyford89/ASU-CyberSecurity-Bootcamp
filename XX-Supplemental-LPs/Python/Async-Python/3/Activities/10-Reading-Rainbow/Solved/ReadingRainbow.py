# Ask the user for a color and save it to a variable
color = input("What color would you like to look up? ")

# Check that the color entered is one of the colors with an associated file
if (color == "red" or color == "orange" or color == "yellow" or color == "green" or color == "blue" or color == "violet"):
# We could also do this with a list i.e.
# if color in ["red", "orange", "yellow", "green", "blue", "violet"]:

    # Create a read-only connection to the file that the user entered
    # Since the files are all in the "Colors" folder the path should be "Colors/<Input>.txt"
    colorFile = open("Colors/" + color + ".txt")

    # Read in the text contained within the colorFile
    colorText = colorFile.read()
    print(colorText)

    # Close the connection to the colorFile
    colorFile.close()

# If there is no file associated with the color entered then print out an apology to the screen
else:
    print("Sorry! There is no associated file for that color.")