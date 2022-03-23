# Part 1: Integers
# =====================================

# Prints: 10
# Prints: # <class 'int'>
variable_one = 10
print(variable_one)
print(type(variable_one))

# Prints: 5
variable_two = 5
print(variable_two)

# Prints: 15
sum_of_variables = variable_one + variable_two
print(sum_of_variables)

# Prints: 5
difference_of_variables = variable_one - variable_two
print(difference_of_variables)

# Prints: 2.0
# Prints: # <class 'float'>
division_variables = variable_one / variable_two
print(division_variables)
print(type(division_variables))

# Prints: 50
multiplication_variables = variable_one * variable_two
print(multiplication_variables)


# Part 2: Floats
# =====================================

# Prints: 1.25
# Prints: # <class 'float'>
variable_three = 1.25
print(variable_three)
print(type(variable_three))

# Prints: 2.25
# Prints: # <class 'float'>
variable_sum = variable_three + 1
print(variable_sum)
print(type(variable_sum))


# Part 3: Strings
# =====================================

# Prints: This is some nifty text!
# Prints: # <class 'str'>
variable_four = "This is some nifty text!"
print(variable_four)
print(type(variable_four))

# Prints: This is also some sweet text!
variable_five = "This is also some sweet text!"
print(variable_five)

# Prints: This is some nifty text! This is also some sweet text!
joined_vars = variable_four + " " + variable_five
print(joined_vars)

# Prints: My favorite number is 14
this_will_work = "My favorite number is " + str(14)
print(this_will_work)

# Prints: 203.1459
text_int = "200"
text_float = "3.1459"
adding_together = int(text_int) + float(text_float)
print(adding_together)

# Part 4: Strings and Integers
# =====================================

# Bonus: Why will the below statement not work (if you uncomment it)
# will_not_work = "My favorite number is " + 14
# print(will_not_work)

# Answer: Strings and Integers cannot be combined without type casting (converting variable types)
