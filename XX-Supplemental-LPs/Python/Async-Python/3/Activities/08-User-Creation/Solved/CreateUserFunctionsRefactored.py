# Copy and paste your `validate_password` function here
def validate_password(password):
    # Inside the function, check if the password is longer than 6 characters long
    if (len(password) > 6):
        return True
    else:
        return False

def collect_user_information():
    # Prompt the user for their username
    username = input("What's your username? ")
    # Prompt the user for their email
    email = input("What's your email? ")
    # Prompt the user for their password
    password = input("What's your password? ")

    # The list that will store all of the user's data inside of it
    user_info = [username, email, password]

    # Return a list with username, email, and password
    return user_info

def create_user(user_data):
    username = user_data[0]
    email = user_data[1]
    password = user_data[2]

    # Use your `validate_password` function to check if the password is secure
    if validate_password(password):
        # If so, create a dictionary, called `user` with the keys "Username", "Email", and "Password"
        # Associate these keys with the values the user entered
        user = {
            "Username": username,
            "Email": email,
            "Password": password
        }
        # When you're done, use `items` to print: `"Your username is <username>"`; `"Your email is <email"`; and `"Your password is <password>"`
        for key, value in user.items():
            print("Your " + key + " is: " + value + ".") 

        # Return user
        return user

    # If the password is too short, tell the user to try again
    else:
        print("Your password is too short, try again!")


# Get user information
user_data = collect_user_information()

# Create user
user = create_user(user_data)


