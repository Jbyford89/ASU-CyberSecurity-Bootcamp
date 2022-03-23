# Master Password
master_password = "password"

# Capture a user's password
# Remember, input is always a string type
password = input("What is your password? ")

# Check if the user's password matches the master_password. Inform user of outcome.
if (password == master_password):
  print("You have been granted access!")

else:
  print("You have been denied access!")

