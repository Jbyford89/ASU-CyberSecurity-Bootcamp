# Create a web address and store it in a variable
URL = "www.mycoolsite.com"

# Store the IP address within a string variable
IP_address = "216.3.128.12"

# Create some variables to store how many times the site was visited each day
monday = 103
tuesday = 126
wednesday = 97
thursday = 458
friday = 78

# Add up all the daily hits for the week and store them in a variable
weekly_hits = monday + tuesday + wednesday + thursday + friday

# Find the average daily hits for the week
average_hits = weekly_hits / 7

# Print all of the summaries to the screen
print("URL: " + URL)
print("IP: " + IP_address)
print("Weekly Hits: " + str(weekly_hits))
print("Average Hits: " + str(average_hits))


# Bonus
# What if we want to print average hits without decimals?

average_hits_int = int(weekly_hits/7)
print("Average Hits as int: " + str(average_hits_int))
