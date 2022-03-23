# Define a function called `validate_password` which accepts a `password`
def validate_password(password):
    # Inside the function, check if the password is longer than 6 characters long
    if (len(password) > 6):
        # If it is, return `True`
        # This is a boolean value
        return True
    else:
        # Otherwise, return `False`
        # This is a boolean value
        return False

# Collect a password to check from the user
passwordToCheck = input("Enter the password to check: ")

# Check if the password is valid and store result into a variable
result = validate_password(passwordToCheck)

# Print the result to the terminal
print(result)
