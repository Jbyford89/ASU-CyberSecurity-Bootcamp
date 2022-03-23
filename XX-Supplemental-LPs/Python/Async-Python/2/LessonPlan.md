##  Lesson 2: Picking Up the Python Pace

### Overview

Today's lesson will pick up the Python programming pace by introducing conditionals and loops. 

### Objectives

By the end of this lesson, you will be able to:

- Use simple and complex conditionals to create branching paths for programs to execute. 
- Build a command-line application using conditionals and user input.
- Use `for` and `while` loops to iterate through lists and dictionaries to perform basic operations on collections of data.
- Use the `range` function to loop through a list with defined ranges. 
- Use the `enumerate` function to loop through a list with a built-in counter. 
- Use `key`, `value`, and `item` methods with loops to convert data from dictionaries into lists.


### Table of Contents

1. [Challenge: Doling Out Data Types](###01.-Challenge-Doling-Out-Data-Types?)
2. [Simple Conditionals](###-02.-Simple-Conditionals)
3. [Challenge: Password Check](###-03.-Challenge-Password-Check)
4. [Complex Conditionals](###-04.-Complex-Conditionals)
5. [Challenge: Bad Bartending](###-05.-Challenge-Bad-Bartending)
6. [For Loops](###-06.-For-Loops)
7. [Range and Enumerate](###-07.-Range-and-Enumerate)
8. [Challenge: Vulnerable List](###-08.-Challenge-Vulnerable-List)
9. [Nested For Loops](###-09.-Nested-For-Loops)
10. [Challenge: Programmer Loop](###-10.-Challenge-Programmer-Loop) 
11. [While Loops](###-11.-While-Loops)
12. [Challenge: The Number Chain](###-12.-Challenge-The-Number-Chain)
13. [Challenge: Kid in a Candy Store](###-13.-Challenge-Kid-in-a-Candy-Store)

### Setup Notes

Refer to instructions in Day 1 for VM and setup notes. 

----

### 01. Challenge: Doling Out Data Types

Before we explore any new concepts, we'll start with a warm-up activity based what we've learned so far.

- In this challenge, you will create a variety of variables and print the information contained within them.

Open the following file in VS code:

  - [DolingOutData.py](Activities/01-Doling-Out-Data/Unsolved/DolingOutData.py)

#### Instructions

Using the provided script, complete the following:

1. Declare a variable called `name` and store your name inside it. 
    - Print the message: "My name is [your name here]."

2. Declare a variable called `age` and store your age inside it.
   - Print the message: "I am [your age here] years old."

3. Declare two variables called `pizza_price` and `number_of_pizzas` and store numbers inside them. Then, store the total price for all the pizzas in a variable called `total_price_of_pizzas`.

    - Print the following messages: 
      - "The price of pizza is [price of pizza] dollars."
      - "We are buying [number of pizzas] pizzas."
      - "The total price for all the pizzas is [total price of pizzas]."

4. Create a list called `favorite_countries`. Store the name of four countries inside it.
   - Print the message: "My favorite countries are [list of countries]."

5. Create a dictionary called `contact_information` and store a home phone number, a cell phone number, and an email address inside it.
    - Print out the message: "Please contact me at [email] or call me at [home number]."
    - Print the message: "In case of an emergency, call [cell number]."


#### Walkthrough

Compare your script with the following solved script: 

  - [Solved: DolingOutData.py](Activities/01-Doling-Out-Data/Solved/DolingOutData.py) 

Refer to the following walkthrough: 

1. For the first two items, we can use a variable and a print statement:

    ```python
    # Declare a variable called `name`, and store your name inside it.
    name = "Peleke"

    # Print the message: "My name is <Your name here>"
    print("My name is " + name + "."
    ```

2. Since the `age` variable is most likely an integer, it needs to be converted into a string before being added to its associated print statement. If we don't do this, we'll get an error.

    ```python
    # Declare a variable called `age` and store your age inside it.
    age = 42

    # Print the message: "I am <Your age here> years old."
    print("I am " + str(age) + " years old.")
    ```

3. The same is true of the `pizza_price`, `number_of_pizzas`, and `total_price` variables. Since these are all integers, they must also be converted into strings before being passed into their print statements.

    ```python
    # Declare a variable called `pizza_price` and store a number inside it.
    pizza_price = 12

    # Declare a variable called `number_of_pizzas` and store a number inside it.
    number_of_pizzas = 4

    # Store the total price for all the pizzas in a variable called `total_price_of_pizzas`.
    total_price = number_of_pizzas * pizza_price

    # Print the message: "The price of a single pizza is $<Price of pizza>."
    print("The price of a single pizza is $" + str(pizza_price) + ".")

    # Print the message: "We are buying <Number of pizzas> pizzas."
    print("We are buying " + str(number_of_pizzas) + " pizzas.")

    # Print the message: "The total price for all the pizzas is <Total price of pizzas>."
    print("The total price of pizza is $" + str(total_price) + ".")
    ```

4. While it would be acceptable to print out each element in the `favorite_countries` list individually using their index, it is also possible to convert the entire list to a string and print that instead.

    ```python
    # Create a list called `favorite_countries`. Store the name of four countries inside it.
    favorite_countries = ["Norway", "Spain", "Taiwan", "Morocco"]

    # Print the message: "My favorite countries are: <Your list here>."
    print("My favorite countries are: " + str(favorite_countries) + ".")
    ```

5. Referencing the values stored within a dictionary is similar to referencing an element stored within a list. However, instead of using a numeric index, each value has an associated string index as its key.

    ```python
    # Create a dictionary called `contact_information` and store a home phone number, a cell phone number, and an email address inside of it.
    contact_information = {
      "email": "BoBoTheClown@gmail.com",
      "cell_number": "203-976-0988",
      "home_phone": "203-867-5309"
    } 

    # Print out the message: "Please contact me at <Email> or call me at <Home phone>"
    print("Please contact me at " + contact_information["email"] + " or call me at " + contact_information["home_phone"])

    # Print out the message: "In case of an emergency call <Cell number>"
    print("In case of an emergency, call " + contact_information["cell_number"])
    ```

---

### 02. Simple Conditionals

In more complex programs, we can assign code to run only when certain conditions are met. We use **conditionals** to run this assigned code. Nearly every conditional statement starts with `if`. 

  ```python
    if (x == 1):

      # code to run is condition is true
  ```   

Point out that while `=` is used for variable assignment, `==` is used for a conditional. `=` means 'Assign the value on the right to the name on the left.' `==` means 'is the item on the left equal to the item on the right?'

Open the following script in VS Code for an overview of basic conditional statements: 

- [SimpleConditionals.py](Activities/02-Simple-Conditionals/SimpleConditionals.py)

Consider the following about the syntax and structure of simple conditionals:

- The equation after the `if` statement is called the **condition**. If true, this statement will cause the code block below the condition to run. If the condition is false, the code block will not run.

- The colon after the condition is required in Python. It separates the condition from the body of code that follows.

- The lines of code after the colon must be indented. It is standard in Python to use four spaces for indenting, but any kind of indentation will work as long as it is consistent.

- When the script reaches code that is not indented, the conditional is considered to have ended. 

  ```python
    if (name == Alice):

        print("Hi, Alice")
  ```   

Sometimes we will want to execute a different block of code if the `if` condition evaluates as false.

  - For this, we need to use an  `else` statement:

    ```python
      if (x == 1):

          # code to run if condition is true

      else 

          # code to run if condition is false

    ```   
  - The `else` statement cannot be used on its own. It must follow an `if` statement and can only be used once per conditional block. In other words, you can't have two `else` statements in one conditional block.

  - The indented code stored after the `else` statement only runs when the preceding `if` condition fails.

  - The `else` statement can be seen as a kind of safeguard for conditionals because it does not require any specific condition to be met. It simply requires the previous conditions to fail.


#### Conditionals Script

Create a new Python script named `my_conditionals.py` and add the code blocks below to your script. Remember to type out the code rather than copy and paste.

1. Start by creating two variables, `x` and `y`. These variables we will be compared with each other to compose our `if` statements. 

    ```python
    x = 1
    y = 10
    ```

2. The `==` operator indicates that the value of one variable is equal to another.  If the values are equal, the conditional statement will evaluate as true. 

    ```python
    # == evaluates to true if the two values are equal
    if (x == 1):
        print("x is equal to 1")
    ```

3. The `!=` operator indicates that the value of one variable is not equal to another. If the values are not equal, the conditional statement will evaluate as true.

    ```python
    # != evaluates to true if the two values are NOT equal to each other
    if (y != 1):
        print("y is not equal to 1")
    ```

4. The `<` operator indicates that the value of one variable is less than another.

    ```python
    # Checks if one value is less than another
    if (x < y):
        print("x is less than y")
    ``` 

5. The `>`  operator indicates that the value of one variable is greater than another.

    ```python
    # Checks that one value is greater than another
    if (y > x):
        print("y is greater than x")
    ```

6. The `<=` operator indicates that the value of one variable is less than or equal to another, and the `>=` operator indicates the opposite. 

    ```python
    # Checks that a value is greater than or equal to another
    if (x >= 1):
        print("x is greater than or equal to 1")
    ```

7. In many cases, if the `if` condition evaluates as false, we will want another block of code to execute instead. For this, we need to use an  `else` statement. 

    ```python
    # If - Else statement
    # The else block of code will only run when the if statement is false
    if (x > 5):
        print("x is large")
    else:
        print("x is small")
    ```


8. Save your script and run it to see its output:

    ```bash
    python3 my_conditionals.py
    x is equal to 1
    y is not equal to 1
    x is less than y
    y is greater than x
    x is greater than or equal to 1
    x is small
    ```

---

### 03. Challenge: Password Check

In this challenge you will create a command-line application that will ask users for their password and check it against the correct password. To do this, it will store users' password response in a variable, and check to see whether this value matches the master password.

Use the following script: 

- [PasswordCheck.py](Activities/03-Password-Checker/Unsolved/PasswordCheck.py)

#### Instructions

- Use the `PasswordCheck.py` file to create a command-line application that asks users for their password. 

    - If the password matches the value stored within the `master_password` variable, alert the user with a message stating: "You have been granted access!"

   - If the password does not match the value stored within the `master_password` variabe, alert the user with a message stating: "You have been denied access!"


#### Walkthrough 

Compare your script to the following solved script: 

- [Solved: PasswordCheck.py](Activities/03-Password-Checker/Solved/PasswordCheck.py)

Refer to the following walkthrough: 

1. Create a variable that holds the password we want to check.

    ```python
    # Master Password
    master_password = "password"
    ```

2. The application needs to use `input()` to capture the user's password within a variable.

    ```python
    # Capture a user's password
    # Remember, input is always a string type
    password = input("What is your password? ")
    ```

3.  Create a conditional statement that checks whether the user's password matches the value stored within the `master_password` variable. If it matches, we grant access. If it doesn't match, we deny access. 

    ```python
    if (password == master_password):
      print("You have been granted access!")

    else:
      print("You have been denied access!")
    ```

      - `if (password == master_password):` starts our conditional statement and compares the values of our two variables.
      - `print("You have been granted access!")` runs if our condition evaluates to true.
      - `else` indicates the code that is run when the entered password does not match `master_password`. 
      - `print("You have been denied access!")` runs if the condition is false.

---

### 04. Complex Conditionals


Additional conditionals such as `or` and `and` allow our programs to perform more complex behavior. 
- These complex conditionals are used when you have more than one condition to check. 
- For example, if we want two separate conditions to pass before executing code, we can use the `and` keyword. 


Open the following script in VS Code for an overview of basic conditional statements: 

- [ComplexConditions.py](Activities/04-Complex-Conditionals/ComplexConditions.py)


#### Complex Conditionals Script 

Close the file and create a new script named `complex_conditionals.py`. Add the code blocks below to your script. Remember to type out the code rather than copy and paste.

1. Create two new variables to work with.
  

      ```python
      x = 1
      y = 10
      ```

2. `and` is used when we want two conditions to evaluate as true before executing the proceeding code. 

      ```python
      # Checks that both conditions are met using "and"
      if (x == 1 and y == 10):
        print("Both values returned true")
      ```

3. If you only need one of multiple conditions to pass, you can use the `or` keyword. `or` only requires one of the conditions to evaluate as true for the entire conditional statement to evaluate as true.


      ```python
      # Checks if either of two conditions are met using "or"
      if (x < 45 or y < 5):
        print("One or more of the statements were true")
      ```

4. The `elif` statement allows you to check multiple, separate conditions for a true evaluation. The code stored after a true `elif` statement only runs when all preceding `if` and `elif` conditions have failed. Any number of `elif` statements can be chained together to account for any number of precise conditions.

      ```python
      if (y < 5):
        print("y is less than 5")
      elif (y == 5):
        print("y is equal to 5")
      else:
        print("y is greater than 5")
      ```

      - `if (y < 5):` is the first condition.
      - `print("y is less than 5")` runs if the first condition is met.
      - `elif (y == 5):` is the second condition.
      - `print("y is equal to 5")` runs if the first condition fails and the second condition is met.
      - `else: print("y is greater than 5")` runs if no conditions are met.


5. Nested `if` statements allow you to check for conditions within a conditional block. Nested conditionals are primarily used to create increasingly specific pathways for code to follow that may not otherwise be possible with `and`/`or` keywords.

    - While we can use any number of nested conditionals, too many can create increasingly confusing code. We can usually use other methods to reduce this complexity.


      ```python
      # Nested if statements allow for more specific conditional pathways
      if (x < 10):
        # We only get here if the value of x is less than 10
        if (y < 5):
            print("x is less than 10 and y is less than 5")
        elif (y == 5):
          # We only get here if the value of x is less than 10 AND
          # the value of y is not less than 5
            print("x is less than 10 and y is equal to 5")
        else:
          # If x is less than 10 but none of the nested conditionals are true
            print("x is less than 10 and y is greater than 5")
      ```

        - `if (x < 10):` starts the first statement. Everything else will run only if this condition returns true.
        - `if (y < 5):` starts the second conditional. This conditional has two options: `elif` and `else`.
        - `print("x is less than 10 and y is less than 5")` runs if the first two conditionals return true.
        - `elif (y == 5):` is the third conditional.
        - `print("x is less than 10 and y is equal to 5")` runs only if the first conditional is true _and_ the third conditional is true.
        - `else: print("x is less than 10 and y is greater than 5")` runs if the first condition is true, and no other conditions are met.

6. The `in` keyword allows you to check for a specific value inside a list or a dictionary. 

      ```python
      if (x in [1,2,3,4,5,6,7]):
        print("The value of x was inside of the list")
      else:
        print("The value of x was not inside of the list")
      ```
    - `if (x in [1,2,3,4,5,6,7]):` states that if the value of the variable `x` is found in our list of numbers, run the following command. 
    - `print("The value of x was inside of the list")` runs if the first condition is true.
    - `else: print("The value of x was not inside of the list")` runs if the first condition is false.

7. Run your script to see its output:

    ```bash
    $python3 complex_conditions.py
    Both values returned true
    One or more of the statements were true
    y is greater than 5
    x is less than 10 and y is greater than 5
    The value of x was inside of the list
    ```

---

### 05. Challenge: Bad Bartending

In this challenge, you will create a digital bartender. This application will first ask the user for their age to determine if they can be served drinks. It will then ask for the user's order. If the order is in the known list of drinks, it will print "Cheers!" to the terminal.

Use the following starter script to build your application: 

- [BadBartending.py](Activities/05-Bad-Bartending/Unsolved/BadBartending.py) 

#### Instructions

1. Set a variable called `drinking_age` to 21.

2. Prompt the user to input their age in years. Then, check if the user is 21 or older.

3. If the user is 21 or older, create a list called `drinks` and store the names of four cocktails inside it. Then, prompt the user to input the drink they want. 

4. Check if the user's selection is in the `drinks` list, and print "Cheers!" to the terminal if it is.

5. If the user is not 21 or older, print "Your fake ID looks really fake." to the terminal instead.

Use the script file provided to get started. It includes the initial code as well as some important pieces throughout. Use the comments to help you with the rest of the code.

#### Walkthrough

Compare your script to the following solution script: 

- [Solved: BadBartending.py](Activities/05-Bad-Bartending/Solved/BadBartending.py)

Refer to the following walkthrough:

1. Start by setting a variable:

    ```python
    # Set a variable called `drinking_age` to 21
    drinking_age = 21
    ```

2. Convert the user's inputted age to an integer. Nest the `input()` function within an `int()` function. This will convert the string input into an integer stored as the `user_age` variable.

    ```python
    # Prompt the user for their age
    user_age = int(input("How old are you? "))
    ```

3. The first `if` statement checks whether the value of the `user_age` variable is greater than or equal to 21. As long as this is true, the application will continue. 

    ```python
     # Check if the user is 21 or older
     if user_age >= 21:

    ```

4. Create a list and ask the user to input a selection.

    ```python
    if user_age >= 21:
        # If so, create a list, called `drinks`. Store four cocktails in it.
        drinks = ["Mai Tai", "Dark and Stormy", "Minotauro", "Old Fashioned"]
        
        # Prompt the user for the drink they want to order
        user_drink = input("What's your order? ")
    ```

5. Use a nested `if` statement to check if their inputted drink is inside of the `drinks` list. 

    ```python
        # Check if the user's selection is in `drinks`
        if user_drink in drinks:
            # If so, print: `"Cheers!"`
            print("Cheers!")
        else:
            # Print: `"I don't know that one..."
            print("I don't know that one...")
    ```

6. Use `else` to print a message if the first `if` statement is false. 

    ```python
    else:
        # If not, print: "Your fake ID looks really fake."
        print("Your fake ID looks really fake."
    ```

---

### 06. For Loops

Having to type the same line of code multiple times is bad practice. We should always aim for clean and concise code. For example, if we have three items that we want to print, we wouldn’t create three print statements. Instead, we would put those items in a list and loop through the list.

- Loops allow programmers to run a block of code multiple times without having to repeatedly type that block of code.

- For example, we have a list of zoo animals and want to print them to the terminal one at a time. We _can_ write out individual print statements for each element in the list, but that would be inefficient and take up a lot of space. Instead we can use a `for` loop to iterate through the list one element at a time and run each element through the same block of code.

Consider the following before and after code blocks: 

- Before `for` loop:
    ```python
    zoo_animals = ["Zebra", "Rhino", "Giraffe", "Owl"]

    print(zoo_animals[0])
    print(zoo_animals[1])
    print(zoo_animals[2])
    print(zoo_animals[3])

    ```
    ```bash
    # Output
    python zoo.py
    Zebra
    Rhino
    Giraffe
    Owl
    ```

- With `for` loop: 
    ```python
    zoo_animals = ["Zebra", "Rhino", "Giraffe", "Owl"]

    for animal in zoo_animals:
      print(animal)

    ```

    ```bash
    # Output
    python zoo.py
    Zebra
    Rhino
    Giraffe
    Owl
    ```

This example uses the following syntax: `for <temporary variable> in <list>:`.

- The temporary variable is `animal`, which holds a single element from within the list variable. 

- Each time the loop completes, the value of the temporary variable is modified to be the next element in the `zoo_animals` list, until there are no values left.


Let's look at another example:

```python
# Start with a list
vegetables = ["carrots", "peas", "lettuce", "tomatoes"]

# Loop through each item of the list
for vegetable in vegetables:
    print("I love" + vegetable)

# Output:
# I love carrots
# I love peas
# I love lettuce
# I love tomatoes
```

- In this example, we created a list called `vegetables`.

- For each temporary variable in the `vegetables` list, the indented `print` command loops through the list and prints the following strings `I love carrots`, `I love peas`, etc.

---

### 07. Range and Enumerate

The `range()` and `enumerate()` functions create lists of numbers that you can use to loop and accomplish a task. 

`range()` creates a list of numbers given a specified range. 

- The `range(x,y)` function allows programmers to loop through a sequence of numbers where `x` is the starting number and `y` is the number to end _before_.

- The second value entered in the `range()` function is exclusive, meaning the output will not reach that value. 

  - For example, `range(1,10)` will return `[1, 2, 3, 4, 5, 6, 7, 8, 9]`.

- Because each element in a list has an associated index, we can use the `range()` function to loop through a specific set of elements within a list, like below:

  ```python
  hobbies = ["skiing", "dancing", "running", "drawing", "piano", "baking"]

  for x in range(2,5):
  
     print(hobbies[x])

     # prints [2, 3, 4] of our list items: "running", "drawing", "piano"
     # Remember, the index of a list always starts with 0. 0 = skiing, 1 = dancing, etc.
     # Does not print [5] because the second number in a range is exclusive. 
    
  ```   


`enumerate()` loops through items of a list and returns a count of those items, like below: 

  ```python
          hobbies = ["skiing", "dancing", "running", "drawing", "piano"]
          for index, hobby in enumerate (hobbies):
            print(index, hobby)

          # Output
          # 0 skiing
          # 1 dancing
          # 2 running
          # 3 drawing 
          # 4 piano
  ```

  - The syntax looks like this: `for index, <item> in enumerate(<list>):` where  `index` is the number assigned to each value, and `item` is the value of each item in the list.

  - In the above example, `index` is the variable assigned to the count. `hobby` is the variable assigned to each item in the hobbies list.   

  - This output also reflects the indices of the list. In the `hobbies` list, skiing is 0, dancing is 1, etc. 

By default, the `enumerate` function will reflect the indices of the specified list. However, if we want to start the count at 1, we use the following syntax: `enumerate(<list>, <starting number>)`.

  - For example: 

    ```python
        hobbies = ["skiing", "dancing", "running", "drawing", "piano"]

        # Note the 1 to indicate that our count starts at 1
        for index, hobby in enumerate(hobbies, 1):
            print(index, hobby)

        # Output
        # 1 skiing
        # 2 dancing
        # 3 running 
        # 4 drawing
        # 5 piano
    ```

We can also use the two values of the `enumerate` function separately. 

  - For example:

    ```python
            hobbies = ["skiing", "dancing", "running", "drawing", "piano"]

            # Note the 1 to indicate that our count starts at 1
            for index, hobby in enumerate(hobbies, 1):
              print(hobby + " is my #" + index + " favorite hobby")

            # Output
            # skiing is my #1 favorite hobby.
            # dancing is my #2 favorite hobby

    ```
---

### 08. Challenge: Vulnerable List

In this activity, you will create two `for` loops to navigate through a list of vulnerable IP addresses. The first loop uses `range()` to collect the five most vulnerable addresses in the list and the second loop uses `enumerate()` to collect all the IP addresses and print their individual ranks.

Use the following script to get started:

- [VulnerableList.py](Activities/08-Vulnerable-List/Unsolved/VulnerableList.py)

#### Instructions

1. Use `range()` to create a loop using that moves through the first five IP addresses and prints them in order to the screen with their rank.

2. Use `enumerate()` to create a loop that moves through all the IP addresses and prints the vulnerability ranking for each one.

**Hint:** The ranking for an IP address is determined by its position in the list. The first element has a rank of 1, the second has a rank of 2, and so on.


#### Walkthrough

Compare your answers with the following:

- [Solved: VulnerableList.py](Activities/08-Vulnerable-List/Solved/VulnerableList.py)

Use the following walkthrough to review the challenge:

1. The first loop uses `range(0,5)` to loop through the first five elements within the `IP_addresses` list.

    - The first element in a list is located at the 0 index and the fifth element is located at the 4 index.

      ```python
      for x in range(0,5):
      ```

    - The `rank` variable is set equal to the current iteration of the loop plus one, so the element located at index 0 has a ranking of 1 when it's printed.

      ```python
      rank = x + 1
      print("The #" + str(rank) + " IP address is " + IP_addresses[x])
      ```

    - **Note:** In the solution script, we added the statement `print("-------------------")` to separate each section of the output.


2. The second loop uses `enumerate()` to loop through all the addresses within the `IP_addresses` list and sets the counter to start at one. 

  
    ```python
    for counter, address in enumerate(IP_addresses, start=1):
      print("#" + str(counter) + " - " + address)
    ```

      - `for` starts our loop.
      - `counter, address` are our two temporary variables. We are using counter instead of index because we will modify the starting count, making each item's count value different than their index value. Note that you can name these variables whatever you wish.
      - `in` is a loop keyword meaning "for each of these two items _in_ the following list."
      - `enumerate(IP_addresses, start=1):` is our `enumerate()` function taking in the `IP_addresses` list and starting the count at `1`. 
      - `print("#" + str(counter) + " - " + address)` executes for each item in the list. The integer held by our `counter` variable is converted to a string. 

---

### 09. Nested for Loops

Lists can become complicated when multiple lists or complex data types like dictionaries are iterated through each loop at the same time. 

Open the following file to view an example of nested `for` loops:
-  [NestedFor.py](Activities/09-Nested-For-Loops/NestedForLoops.py) 

- Nested loops are loops that contain other loops. These allow you to loop through multiple lists at once and easily compare or combine the values of lists with different lengths. 

These loops works by collecting a value from the first list and looping through the values of the second list. Once it loops through all the values in the second list, Python moves to the next item on the first list and loops it through the second list.


#### Nested Loops Script

Create a new script named `nested_loops.py`. Add the code blocks below to your script.

1. Let's create a few lists. 

      ```python
      # A list of five letters
      letter_list = ["B", "I", "N", "G", "O"]
      # A list of 20 numbers
      numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
      ```

2. Add a nested loop that pairs each of the letters with each of the numbers and print them. Add the following three segments to your script: 

    - Start by adding your first `for` loop:

      ```python
      # The first loop moves through all the letters in the letter list
      for letter in letter_list:
      ```

    - Next, we'll add another `for` loop.  Note that this loop must be correctly indented under the first `for` loop.

      ```python
      for letter in letter_list:
        for number in numbers_list:
      ```

    - Now we can add our `print` statement :

      ```python
      for letter in letter_list:
        for number in numbers_list:
          print(letter + str(number))
      ```

Dictionaries can also store vast quantities of data within them. However, unlike lists, the data stored within dictionaries is not stored with numeric indexes and requires a bit more effort to loop through.

- There are three methods that programmers can use to store dictionary data inside of a list.

  - The `dictionary.keys()` method collects all the keys from a dictionary and places it into a list.

  - The `dictionary.values()` method collects all the values from a dictionary and places them into a list.

  - The `dictionary.items()` method collects both the keys and the values from a dictionary and places them into a list. Because this has both the keys and the values in it, two temporary variables have to be used when looping through the collection.

3. Let's create a dictionary to examine how these work. 


    ```python
    my_nemesis = {
        "Weakness": "Kryptonite",
        "Greatest Fear": "Spiders",
        "Secret Lair": "300 Nemesis Drive #665"
    }
    ```
 
4. Now that we have a dictionary, we'll try the `.keys()` method. To extract our keys, we can call `.keys()` on our dictionary and assign it to a new variable. 


    ```python
    key_list = my_nemesis.keys()
    ```

   - This variable will hold a list of only the keys from the dictionary: `["Weakness", "Greatest Fear", "Secret Lair"]`

   - Now we can loop through this list:

      ```python
      for key in key_list:
        print(key)
      ```

5. Similarly, we can use the `.values()` method to extract only the values: 

      ```python
      value_list = my_nemesis.values()
      ```

    - This variable will now hold a list of the values from the dictionary: `["Kryptonite", "Spiders", "300 Nemesis Drive #665"]`

    - We can loop through it with:

      ```python
      for value in value_list:
        print(value)
      ```

6. If we want to use both keys and values at the same time, we use the `.items()` method. 

    - We can call `.items()` directly in our loop without the use of a variable. Note that just like with `enumerate`, we need to use two variables with `.items`. For example: `for key, value in dictionary.items():`

  - Let's add the following code that uses more creative variable names:

    ```python
    for item, juicy_tidbit in my_nemesis.items():
        print("My nemesis's " + item + " is " + juicy_tidbit + ".")
    ```

7. Run the script to see its output:

    ```bash
    $ python3 nested_loops.py 
    B1
    B2
    B3
    B4
    B5
    B6
    ...<truncated>

    I have dirt on my nemesis's...
    Weakness
    Greatest Fear
    Secret Lair
    To ruin my rival's life, you need to know about...
    Kryptonite
    Spiders
    300 Nemesis Drive #665
    My nemesis's Weakness is Kryptonite.
    My nemesis's Greatest Fear is Spiders.
    My nemesis's Secret Lair is 300 Nemesis Drive #665.
    ```
---

### 10. Challenge Programmer Loop 

- In this activity, you will use nested `for` loops to print the contents of dictionaries.  

- You will be given a short list of dictionaries of people who work as programmers. 

- You must print out all the key-value pairs for each programmer using a series of nested `for` loops.

Open the following file in VS Code: 
- [ProgrammerLoop.py](Activities/10-Programmer-Loops/Unsolved/ProgrammerLoop.py)

#### Instructions

Using the list of dictionaries in the provided script, do the following:

1. Loop through the `programmers_list` one dictionary at a time.

2. Loop through each of the dictionary's keys and values.

3. Print each key and its associated value to the terminal.

4. Print a line to separate each programmer.
 
Some code has been added to the script file. Use the comments to help you with the rest. 

#### Walkthrough

Compare your script with the following solved script:
- [Solved: ProgrammerLoop.py](Activities/10-Programmer-Loops/Solved/ProgrammerLoop.py)

Use the following walkthrough to review the challenge: 

1. You were given a list of dictionaries and asked to print different items from it. The dictionary is: 

    ```python
    programmer_list = [
      {
        "name": "Jacob Deming",
        "age": 27,
        "fave_language": "Python",
        "skill_level": 80
      },{
        "name": "Billy Bob",
        "age": 30,
        "fave_language": "True Basic",
        "skill_level": 120
      },{
        "name": "Kelsey Queen",
        "age": 25,
        "fave_language": "C++",
        "skill_level": 83
      }
    ]
    ```

    - We can see that there are three items in the list. They will have indices 0-2. Each dictionary has the same keys. 

2. To loop through the `programmer_list` one dictionary at a time, use the following `for` loop:

    ```python
    for programmer in programmer_list:
    ```

    - Each time this loops, our `programmer` variable gets assigned a new list item. Since each list item is a dictionary,  we can treat our `programmer` variable as if it were a dictionary. Therefore, we can use dictionary methods such as `.keys()`, `.values()` and `.items()`.

3. To loop through each dictionary's keys and associated values, use a nested `for` loop:

    ```python
    for key, value in programmer.items():
    ```
      - `programmer.items()` is using the `programmer` variable from the first `for` loop and applying the `.items()` method to it, because it will contain a dictionary from our list of dictionaries. 

4. To print out the key and its value to the terminal, use the `print` statement and the `key` and `value` variables:

    ```print
    print(key + ": " + str(value))
    ```
    - You will need to convert integer values to strings. The `str()` function will not affect the values that are already strings.

5. To add a line between each new programmer in the list, use a simple `print` statement:

    ```python
    print("---------")
    ```

6. Without comments, the nested `for` loop should look like this:

    ```python
    for programmer in programmer_list:
      for key, value in programmer.items():
        print(key + ": " + str(value))
      print("---------")
    ```

    - Note that the second `print` statement is indented under the first loop and not the second.

7. Run the script to view its output:

    ```bash
    $ python3 ProgrammerLoop.py 
    name: Jacob Deming
    age: 27
    fave_language: Python
    skill_level: 80
    ---------
    name: Billy Bob
    age: 30
    fave_language: True Basic
    skill_level: 120
    ---------
    name: Kelsey Queen
    age: 25
    fave_language: C++
    skill_level: 83
    ---------
    ```


### 11. While Loops

All the loops we've looked at so far have iterated through every element of the specified list. The loop repeats as many times as there are items in the list or as many times as we specify. 

- This is the function of a `for` loop: "loop for x amount of times." 

- However, what if we don't know how many times the loop should run?

- What if we want to loop _until_ something else happens?  

The `while` loop says, "while [conditon] is true, loop." As long as the condition evaluates to true, the loop continues. As soon as our condition is false, the loop stops.

Below is a comparison:

```python
  # for loops allow you to run a block of code for each item in a sequence

  sequence = ["a", "b", "c"]

  for item in sequence:
    print(item)

 # while loops allow you to run a block of code while a condition is true

  i = 0

  while i  < 5:
      print(i)
      i  = i+ 1 
```

Let's look at another example:

```python
  i = 1

  # while i is less than five, run this code block

  while i < 5: 
      print(f"I have {i} dollar(s)")
      i = i + 1

  # prints 
  # I have 1 dollar(s)
  # I have 2 dollar(s)
  # I have 3 dollar(s)
  # I have 4 dollar(s)

```  

- Given `i` equals 1, this loop will print the phrase "I have `i` dollar(s)" and then add a value of 1 to `i` until `i` is equal to or greater than 5.  


- Note that this `print()` statement is different. In Python, the `print(f)` is a shortcut to format other data types into a string for ease of printing. 

  - In this example, we want to print a variable, `i`, in our string. Since we can’t interpolate an integer into a string without formatting it, we can use the `print(f)` function to convert any variable surrounded by `{}` into a string. 

Since `while` loops continue as long as a condition is met, a loop can theoretically continue forever. 

- A loop that never ends is called an **infinite loop** and is a common pitfall when beginning to write `while` loops. 

- If you accidentally write an infinite loop in your script, you can force your script to stop by entering Ctrl+C on the command line.


#### While Loops Script

Open [WhileLoops.py](Activities/11-While-Loops/WhileLoops.py) for an overview of using a `while` loop and then create your own script named `while_loops.py`.

- `while` loops are commonly used in creating command-line interfaces. The loop begins and the user is prompted with a question. 

- As long as the answer to the question meets the condition, the loop continues, and the application continues to function. 

- When the user decides to exit, the loop concludes and the application closes.

In the following script, we'll  create a similar command-line interface. Add the code blocks below to your script:

1. Begin by creating a `userInput` variable:

      ```python
      userInput = "yes"
      ```

2. Start the `while` loop. 

      ```python
      while (userInput == "yes"):
      ```

    - This will continue to run our code until the `userInput` variable is something _other_ than `yes`.

    - Note that this loop does not account for `y` or `yea` inputs.

3. Next,  we'll add a message before asking for user input:

      ```python
      print("Round and round we go!")
      print("----------------------"

      userInput = input("Would you care to loop again? (yes or no) \n")
      ```

       - `\n` will create a new line below the printed sentence. 

4. Add a message if the user escapes the loop:

      ```python
      print("You escaped the loop!")
      ```

5. The final code without comments reads:

```python

userInput = "yes"
while (userInput == "yes"):

    print("Round and round we go!")
    print("----------------------")

    userInput = input("Would you care to loop again? (yes or no) \n")

print("You escaped the loop!")
```

- Notice that our last print statement is outside of the `while` loop. It will only run when the loop is broken.

Run the script to see its behavior. Remember, if your loop gets stuck for some reason, press Ctrl+C to quit.

  ```bash
    $ python3 while_loops.py 
    Round and round we go!
    ----------------------
    Would you care to loop again? (yes or no) 
    yes
    Round and round we go!
    ----------------------
    Would you care to loop again? (yes or no) 
    yes
    Round and round we go!
    ----------------------
    Would you care to loop again? (yes or no) 
    no
    You escaped the loop!
  ```

---

### 12. Challenge: The Number Chain

In this challenge, you will build a command-line application that will ask the user for a number and then print all the numbers from zero until that number.

Open this file in VS Code: 
- [TheNumberChain.py](Activities/12-The-Number-Chain/Unsolved/TheNumberChain.py) 

#### Instructions

Using the provided script, complete the following:

1. Ask the user "How many numbers?" Then, print a chain of ascending numbers from zero up to, but not including, the number inputted.

2. After the results have printed, ask the user if they would like to continue. 
    - If `y` is entered, keep the chain running by prompting the user to input a new number and starting a new count from zero to the number inputted. 
    - If `<anything but y>` is entered, exit the application.
  
Some of the initial code is included in the script file. Use the comments to help you with the rest. 

**Bonus:** For users who choose to continue, have counts begin at the number following the final number in the previous sequence. For example: If the first loop printed `0, 1, 2, 3`, the next loop should start the count at `4`.


**Hint:** You will need to use both `for` and `while` loops for this activity. The script provides the start of the `while` loop. 

#### Walkthrough 

Compare your script with the following solved file:
- [Solved: TheNumberChain.py](Activities/12-The-Number-Chain/Solved/TheNumberChain.py)

Use the following walkthrough to review the challenge: 

1. The initial value for `user_play` is set to `y`, so the `while` loop will run at the onset. This loop will continue to run as long as the value of `user_play` is `y` at the end of the code block. Those lines look like this:

    ```python
    # Initial variable to track game play
    user_play = "y"

    # While we are still playing...
    while user_play == "y":
    ```

2. The code will ask for an input number and then a `for` loop will run to count from zero to that number using the `range()` function.

    ```python
    user_number = input("How many numbers? ")
    for x in range(int(user_number)):
        print(x)
    ```


      - `user_number = input("How many numbers? ")` prompts the user to give a number.
      - `for x in range():` is the `for` loop that uses the `range()` function.
      - `int(user_number)` converts the input to an integer. The `range()` function will then create a list of numbers from zero to the number before the inputted integer.
      - `print(x)` will output each number from the list that `range()` returns.

3. At the end of our script, the user should be prompted to enter `y` if they would like to create a new number chain or `n` if they would like to terminate the application. Add another `input()` statement and reassign the `user_play` variable to the new input. Based on the input, the `while` loop will either loop again or stop.

    ```python
    user_play = input("Continue: (y)es or (n)o? ")
    ```

4. Your full script should read similar to:

    ```python
    user_play = "y"

    while user_play == "y":
        user_number = input("How many numbers? ")
        
        for x in range(int(user_number)):
            print(x)

        user_play = input("Continue: (y)es or (n)o? ")
    ```

5. Run the script to see its behavior:

    ```bash
    $ python3 TheNumberChain.py 
    How many numbers? 3
    0
    1
    2
    Continue: (y)es or (n)o? y
    How many numbers? 2
    0
    1
    Continue: (y)es or (n)o? y
    How many numbers? 4
    0
    1
    2
    3
    Continue: (y)es or (n)o? n
    ```

View the following script for the bonus solution: 
- [Bonus: TheNumberChain.py](Activities/12-The-Number-Chain/Solved/BONUS_TheNumberChain.py)

 Add a variable called `start_number` with the initial value of `1`. The value will be set to the last number used in the loop after the `for` loop has completed.

  ```python
    user_number = input("How many numbers? ")
    start_number = 1
  ```

- The `for` loop will run from the range of `start_number` to `user_number` plus `start_number`. This means that the code will always count up the inputted amount from the previous input amount.

    ```python
    for x in range(start_number, int(user_number) + start_number):
        print(x)
    ```

- Set the next start number as the last number of the loop:

    ```python
    start_number = start_number + user_number
    ```

- Your full script should now read:

    ```python
    user_play = "y"
    start_number = 0

    while user_play == "y":
        user_number = int(input("How many numbers? "))
        
        for x in range(start_number, int(user_number) + start_number):
            print(x)

        start_number = start_number + user_number
        user_play = input("Continue the chain: (y)es or (n)o? ")
    ```

- Run the new script to view the output:

    ```bash
    $ python3 BONUS_TheNumberChain.py 
    How many numbers? 3
    0
    1
    2
    Continue the chain: (y)es or (n)o? y
    How many numbers? 2
    3
    4
    Continue the chain: (y)es or (n)o? y
    How many numbers? 4
    5
    6
    7
    8
    Continue the chain: (y)es or (n)o? n
    ```
---

### 13. Challenge: Kid in a Candy Store

For the final challenge of this lesson, you will create a command-line application that simulates a child choosing candy at a candy store with a specific allowance to spend. 

Open the following file in VS Code: 

- [KidInCandyStore.py](Activities/13-Kid-In-Candy-Store/Unsolved/KidInCandyStore.py)

#### Instructions

In this challenge, you will use the following criteria to create a command-line application. 
- There is a specific selection of candies, each costing $1. 
- The user has a $5 allowance. 
- The user will select five candies. Once they have exhausted their allowance, the terminal will print a message stating which candies they purchased.

Turn the requirements below into code: 

1. Print the list of candies provided in the file, with their index numbers in brackets beside them.
    - Create a loop that prints all of the candies in the store to the terminal, with their index numbers in brackets beside them.
    - Example: `"[0] Snickers"`
    - **Note:** This first requirement has already been added to the script file. 

2. Print a prompt that asks “Which candy would you like to buy?” The user will have to input the index associated with the candy. This prompt will run until five choices are made.
    - Create a loop that runs for a number of times as determined by the variable `allowance`. 
      - Example: If `allowance` is equal to five, the loop will run five times.
    - Each time this second loop runs, prompt users to input a number, and add the candy with the matching index to the variable `candyCart`.
      - Example: If the user enters `0` as their input, `"Snickers"` should be added into the `candyCart` list.
 
4. Print a statement that says which candies the user purchased.
    - Create another loop to print all the selected candies to the terminal.

 **Bonus**: Create a version of the same code that allows a user to select as much candy as they want, until they say they do not want any more.

#### Walkthrough


Compare your solution with the following solved file:

- [Solved: KidInCandyStore.py](Activities/13-Kid-In-Candy-Store/Solved/KidInCandyStore.py)

Use the walkthrough to review the solution: 

There are three `for` loops used in this activity. One prints out the original candy list. A second collects all the candy choices the user makes. A third prints the final list of choices to the screen.

1. Start with the list of candies, an allowance, and an empty candy cart:
    ```python
    candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit",
                "Swedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]
    allowance = 5

    candyCart = []
    ```

2. The script gives the first `for` loop that will print each candy along with its index from the list:

    ```python
    for candy in candyList:
        print("[" + str(candyList.index(candy)) + "]" + candy)
    ```


      - `for candy in candyList:` this should be familiar as it is starting our `for` loop.
      - `print()` is also familiar to us.
      - `"["` is adding some format so our index number will be surrounded by `[]`.
      - `str()` converts an integer to a string.
      - `candyList.index(candy)` uses the `.index()` method to return the index of any given list item.
      - `"]"` closes our brackets.
      - `candy` provides the value from the candy variable in any given iteration of the loop.
        - This gives each item in the list a reference number that we can use when adding candy to our cart.

3. Using a second `for` loop, the `range()` function and the `allowance` variable, create a loop that allows users to choose which candies they take home. 

    ```python
    for x in range(allowance):
        selected = input("Which candy would you like to buy? ")
    ```


    - Range will return the list `[0, 1, 2, 3, 4]` through five iterations.

    - Each iteration assigns a variable named `selected` to the value given from an input statement.

4. Add this value to the candy cart during  each iteration. Remember that when we add candies to the `candyCart` list, the `selection` variable has to be made into an integer, since all inputs are naturally set as strings. 

    ```python
    candyCart.append(candyList[int(selected)])
    ```

    - Note: `int()` can only turn number strings into integers. If a user gives a value that isn't a number, the script will break. 

5. To loop through the `candyCart` list and print which candies were brought home, add a `print` statement and start a loop to list all the candies:

    ```python
    print("I bought...")
    for candy in candyCart:
        print(candy)
    ```

6. Your full script should resemble:

    ```python
    candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit",
                "Swedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]
    allowance = 5
    candyCart = []

    for candy in candyList:
        print("[" + str(candyList.index(candy)) + "] " + candy)

    for x in range(allowance):
        selected = input("Which candy would you like to buy? ")

        candyCart.append(candyList[int(selected)])

    print("I bought...")
    for candy in candyCart:
        print(candy)
    ```

7. Run the script to observe its behavior:

    ```bash
    $ python3 KidInCandyStore.py 
    [0] Snickers
    [1] Kit Kat
    [2] Sour Patch Kids
    [3] Juicy Fruit
    [4] Swedish Fish
    [5] Skittles
    [6] Hershey Bar
    [5] Skittles
    [8] Starbursts
    [9] M&Ms
    Which candy would you like to buy? 4
    Which candy would you like to buy? 6
    Which candy would you like to buy? 9
    Which candy would you like to buy? 0
    Which candy would you like to buy? 1
    I bought...
    Swedish Fish
    Hershey Bar
    M&Ms
    Snickers
    Kit Kat
    ```

Review the following script for the bonus solution:

- [Bonus: KidInCandyStore.py](Activities/13-Kid-In-Candy-Store/Solved/BONUS_KidInCandyStore.py)

To solve the bonus, use a `while` loop instead of a `for` loop with the condition asking whether the user would like to make another selection. If they answer anything other than `yes`, the loop will stop.

- The script should resemble the following:

  ```python
  while (more == "yes"):
    allowance = 5

    for x in range(allowance):
        selected = input("Which candy would you like to buy? ")

        candyCart.append(candyList[int(selected)])

    more = input("Would you care to loop again? (yes or no)" \n)
  ```

- In full, your script should look like:

    ```python
    candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit",
                "Swedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]
    candyCart = []
    more = "yes"

    for candy in candyList:
        print("[" + str(candyList.index(candy)) + "] " + candy)

    while (more == "yes"):
      allowance = 5

      for x in range(allowance):
          selected = input("Which candy would you like to buy? ")

          candyCart.append(candyList[int(selected)])

      more = input("Would you care to loop again? (yes or no) \n")

    print("I brought home with me...")
    for candy in candyCart:
        print(candy)
    ```

- An example output:
    ```bash
    python3 BONUS_KidInCandyStore.py 
    [0] Snickers
    [1] Kit Kat
    [2] Sour Patch Kids
    [3] Juicy Fruit
    [4] Swedish Fish
    [5] Skittles
    [6] Hershey Bar
    [5] Skittles
    [8] Starbursts
    [9] M&Ms
    Which candy would you like to buy? 9 
    Which candy would you like to buy? 3
    Which candy would you like to buy? 2
    Which candy would you like to buy? 9
    Which candy would you like to buy? 0
    Would you care to loop again? (yes or no) 
    yes
    Which candy would you like to buy? 6
    Which candy would you like to buy? 5
    Which candy would you like to buy? 3
    Which candy would you like to buy? 9
    Which candy would you like to buy? 0
    Would you care to loop again? (yes or no) 
    yes
    Which candy would you like to buy? 0
    Which candy would you like to buy? 0
    Which candy would you like to buy? 0
    Which candy would you like to buy? 0
    Which candy would you like to buy? 0
    Would you care to loop again? (yes or no) 
    n
    I purchased...
    M&Ms
    Juicy Fruit
    Sour Patch Kids
    M&Ms
    Snickers
    Hershey Bar
    Skittles
    Juicy Fruit
    M&Ms
    Snickers
    Snickers
    Snickers
    Snickers
    Snickers
    Snickers
    # From this output we can see that Snickers is the best candy
    ```
---

Good work completing the second lesson of Python programming! 

In this lesson, we covered:

- Using simple and complex conditionals to create branching paths for programs to execute. 
- Building a command-line application using conditionals and user input.
- Using `for` and `while` loops to iterate through lists and dictionaries to perform basic operations on collections of data.
- Using the `range` function to loop through a list with defined ranges. 
- Using the `enumerate` function to loop through a list with a built-in counter. 
- Using `key`, `value`, and `item` methods with loops to convert data from dictionaries into lists.

In the final lesson, we will:

- Define and call functions. 
- Create functions to print data from a dictionary.
- Create functions with arguments to make them more modular.
- Create functions with return values.
- Build command-line applications that both return and print values to the user.

-------

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.   