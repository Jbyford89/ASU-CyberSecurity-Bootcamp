## Lesson 3: Python and Functions

### Overview

In this lesson, you will build custom functions. 

### Objectives

By the end of this lesson, you will be able to:

- Define and call functions. 
- Create functions to print data from a dictionary.
- Create functions with arguments to make them more modular.
- Create functions with return values.
- Build command-line applications that both return and print out values to the user.
- Create scripts that open files and read them.
- Chop up strings to find specific words.

### Table of Contents

1. [Challenge: Inventory  Collector](###-01.-Warm-Up:-Inventory-Collector)
2. [Introduction to Functions](###-02.-Introduction-to-Functions)
3. [Challenge: My Very First Functions](###-03.-Challenge-My-Very-First-Functions)
4. [Parameters](###-04.-Parameters)
5. [Challenge: Functional Calculator](###-05.-Challenge-Functional-Calculator)
6. [Returning Values](###-06.-Returning-Values)
7. [Challenge: Validate Password](###-07.-Challenge-Validate-Password)
8. [Challenge: User Creation](###-08.-Challenge-User-Creation)
9. [Read Text Files](###-09.-Reading-Text-Files)
10. [Challenge: Reading Rainbow](###-10.-Challenge-Reading-Rainbow) 
11. [String Function](###-11.-String-Functions)
12. [Challenge: Word Search](###-12.-Challenge-Word-Search)


---

### 01. Warm-Up: Inventory Collector 

We will start the day off with a warm-up challenge based on the material from the last lesson.

In this challenge, you will create an application that allows its users to create and fill in a store's inventory, and print the inventory to the terminal.

Open the following script in VS Code:

- [InventoryCollector.py](Activities/01-Inventory-Collector/Unsolved/inventorycollector.py)

#### Instructions

1. Create an empty dictionary called `inventory`.

2. Ask the user how many items they have in their inventory and store it in a variable called `item_count`.

     - You will need to create a `for` loop and use `range` to loop over the item count.

3. For each item, ask the user for the item name and price.

     - Store the item name as a variable called `item_name` and  the item price as a variable called `item_price`.     

      - **Note:** Item prices must be entered as integers and not strings.

4. Create a dictionary that has the item name and item price as its key-value pair.

5. Print the key-value pair to the console. For each item less than five dollars, indicate that the item is on sale.

    - You will need to loop through all the items in the dictionary and print your key-value pairs to the console.

     - Inside of this loop, you will also need to create a conditional that checks the price.

#### Walkthrough 

Compare your script with the solved file:

-  [Solved: inventorycollector.py](Activities/01-Inventory-Collector/Solved/inventorycollector.py) 


Use the following walkthrough to review the steps: 

1. Start with an empty `inventory` dictionary, an `item_count` input statement, and a `for` loop set to iterate through a list created by feeding our return `item_count` number into `range()`.


    ```python
    inventory = {}

    item_count = int(input("How many items do you have in your inventory? "))

    for x in range(item_count):
    ```

    - `range()` specifies how many iterations of the loop should take place. The number of iterations is determined by the first `input()` and the response is converted to an integer using `int()`.


2. Next, the user will enter the name of the item and its price. We are using `item_name` and `item_price` to create the new key-value pair inside of `inventory`.

    ```python
    item_name = input("What's the item? ")

    item_price = input("What's its price? ")

    inventory[item_name] = float(item_price)
    ```

3. A second loop will iterate through both the keys and the values of the `inventory` dictionary using the `.items()` method.

    ```python
    for item, price in inventory.items():
        print("The price of " + item + " is $" + str(price))
    ```

4. To add a message if the item is on sale, use an `if` statement to check the price of the current item and compare it to the number five. If the value is greater than five, nothing happens. If the value is less than five, a new line is printed to the terminal.

    ```python
    if (price < 5):
        print("This item is on sale!")
    ```

5. You can add a few print statements to help format the output.

    ```python
    print("--------"
    ```

6. Your final script should be similar to:

    ```python
    inventory = {}
    item_count = int(input("How many items do you have in your inventory? "))

    for x in range(item_count):
        item_name = input("What's the item? ")
        item_price = input("What's its price? ")
        inventory[item_name] = float(item_price)

        print("--------")


    for item, price in inventory.items():
        print("The price of " + item + " is $" + str(price))

        if (price < 5):
            print("This item is on sale!")

        print("--------")
    ```

7. Run your script to view its output:

    ```bash
    $ python3 inventory_collector.py 
    How many items do you have in your inventory? 3
    What is the item? banana  
    What is its price? 3
    --------
    What is the item? apple
    What is its price? 6
    --------
    What is the item? orange
    What is its price? 8
    --------
    The price of banana is $3.0
    This item is on sale!
    --------
    The price of apple is $6.0
    --------
    The price of orange is $8.0
    --------
    ```


### 02. Introduction to Functions

One of the most important qualities of easy-to-understand code is that it avoids repetition. 

Key to this are **functions**, which are blocks of organized, reusable code that can be used to perform a single action multiple times.

We've already used a variety of pre-packaged Python functions. For example, we used `print()` to post data to the terminal and `input()` to get data from the user.

- But programmers will also want to create their own functions for more specific use cases. These are commonly referred to as **user-defined functions**.

The following script provides an overview of functions:

- [IntroToFunctions.py](Activities/02-Intro-To-Functions/IntroToFunctions.py) 

The first step is to **define** our functions. 

- To define a function, we use the `def` keyword followed by the function's name and a pair of parentheses. The block of code contained within the function must be indented and start with a colon. This is the same colon and indentation syntax we use with `if` statements and `for` loops. 

    ```python 
    def printHello():
       print("Hello User!")
       print("You have just defined and called your first function!")
       print("Great job!")
    ```

Defining a function in our file does not guarantee that it will run.

- In the `IntrotoFunctions.py` file, remove `printHello()` at the bottom of the file.  Save and run the file. Nothing will happen.

- Code can only be executed when we **call** the function later in the script. Add `printHello()` back to the script. Save and run the file. The output should read on the screen. 

#### Scope

Not all variables are accessible to all parts of our program. Scope defines how accessible a variable is. A variable's scope refers to the places that the application can see/access a specific variable.

- For example, if you define a variable at the top of your program or in the main body of your program, it is considered a **global variable**.  Global variables can be used by any function.

- If a variable is defined within a specific function, it is a **local** variable. A local variable is only accessible to the function that it was defined in. Other parts of the program cannot access it.

- Open the following script:
  - [Scope.py](Activities/02-Intro-To-Functions/Scope.py) 


- The `global_variable` at the top of the file is outside the scope of the function, but still accessible within the function. This means that it was not defined inside the function `printPhrases()`. 

    ```python
    global_variable = "I can go anywhere!"

    def printPhrases():
    ```
  
- The `local_variable` is only accessible within the  `printPhrases` function.

    ```python
    global_variable = "I can go anywhere!"

    def printPhrases():

       local_variable = "I only exist in this function!"

       print(global_variable)
       print(local_variable)
    ```

- We can call this function to print both our `global_variable` and our `local_variable`:

    ```python
    printPhrases()
    ```

- We can also call the `global_variable` on its own:

    ```python
    print(global_variable)
    ```

- However, we cannot call the `local_variable` on its own:

    ```python
    print(local_variable) #This will not work
    ```

Run the `Scope.py` script to see the error we receive if we try to use this local variable outside the `printPhrases` function:

```bash
    $ python3 Scope.py 
    I can go anywhere!
    I only exist in this function!
    ----------
    I can go anywhere!

    Traceback (most recent call last):
    File "Scope.py", line 26, in <module>
        print(local_variable)
    NameError: name 'local_variable' is not defined
```

Python doesn't know the value of `local_variable` because it hasn't been defined globally. It is only accessible within the context, or scope, of the `printPhrases` function. 

---

### 03. Challenge: My Very First Functions

In this challenge, you will create three functions used to print valuable information to the terminal.

Open the following file in VS Code: 

- [FirstFunctions.py](Activities/03-First-Function/Unsolved/FirstFunctions.py)
 
#### Instructions
  
Using the provided dictionary of names and social security numbers (SSNs), complete the following tasks:

1. Create a function that will loop through and print all of the keys in the dictionary.
 
2. Create a function that will loop through and print all of the values in the dictionary.
 
3. Create a function that will loop through and print all of the keys _and_ values in the dictionary.
      
**Hints:** 
- You will need to use loops within your functions.

- Remember that you will need to call your functions to execute them.

#### Walkthrough

Compare your script to the following solved file: 

- [Solved: FirstFunctions.py](Activities/03-First-Function/Solved/FirstFunctions.py)

Use the following walkthrough as a review. 

The script provides a dictionary. We needed to finish defining all of the functions and add code to call those functions and view their output.

- Note that all of the loops in this code are `for` loops, which loop through the lists created by calling `keys()`, `values()`, and `items()` in the dictionary.


    ```python
    large_dict = {
    "Tina Flemming": "619-16-7988",
    "Erica Shah": "164-51-7615",
    "Paula Ortiz": "051-83-3290",
    "James Hendricks": "776-83-2884",
    "Lauren King": "197-94-2398",
    "David Cowan": "252-92-1832",
    "Andrew Burton": "296-23-6842",
    "Julian Baker": "337-40-7543",
    "Scott Castro": "399-46-5595",
    "Billy Rodriguez": "014-18-2503",
    "Darrell Leblanc": "005-82-7918",
    "David Hammond": "561-17-6312"
    }


    def printAllKeys():
        for key in large_dict.keys():
            print("Name: " + key)


    def printAllValues():



    printAllKeys()
    print("--------"
    ```


1. Complete the `printAllValues()` function:

    ```python
    def printAllValues():
        for value in large_dict.values():
            print("SSN: " + value)
    ```


    - `def printAllValues():` begins to define the function.
    - `for value in large_dict.values():` begins the `for` loop that loops through just the `values` in the dictionary.
    - `print("SSN: " + value)` prints the output.

2. Define a `printAllItems()` function:

    ```python
    def printAllItems():
        for key,value in large_dict.items():
            print("Name: " + key +  " || SSN: " + value)
    ```


    - `def printAllItems():` begins the function definition. 
    - `for key,value in large_dict.items():` begins the `for` loop and uses `.items` to iterate through both the keys and values of the dictionary.
    - `print("Name: " + key +  " || SSN: " + value)`  prints the statement with specific formats.

3. Call the functions to execute their code:

    ```python
    printAllKeys()
    print("--------")

    printAllValues()
    print("--------")

    printAllItems()
    ```

    - Additional print statements were added to help format the output.

4. Run the script to see its output:

    ```bash
    $ python3 FirstFunctions.py 
    Name: Tina Flemming
    Name: Erica Shah
    Name: Paula Ortiz
    Name: James Hendricks
    Name: Lauren King
    Name: David Cowan
    Name: Andrew Burton
    Name: Julian Baker
    Name: Scott Castro
    Name: Billy Rodriguez
    Name: Darrell Leblanc
    Name: David Hammond
    --------
    SSN: 619-16-7988
    SSN: 164-51-7615
    SSN: 051-83-3290
    SSN: 776-83-2884
    SSN: 197-94-2398
    SSN: 252-92-1832
    SSN: 296-23-6842
    SSN: 337-40-7543
    SSN: 399-46-5595
    SSN: 014-18-2503
    SSN: 005-82-7918
    SSN: 561-17-6312
    --------
    Name: Tina Flemming || SSN: 619-16-7988
    Name: Erica Shah || SSN: 164-51-7615
    Name: Paula Ortiz || SSN: 051-83-3290
    Name: James Hendricks || SSN: 776-83-2884
    Name: Lauren King || SSN: 197-94-2398
    Name: David Cowan || SSN: 252-92-1832
    Name: Andrew Burton || SSN: 296-23-6842
    Name: Julian Baker || SSN: 337-40-7543
    Name: Scott Castro || SSN: 399-46-5595
    Name: Billy Rodriguez || SSN: 014-18-2503
    Name: Darrell Leblanc || SSN: 005-82-7918
    Name: David Hammond || SSN: 561-17-6312
    ```

---

### 04. Parameters 

In the previous challenge, we defined and called the following functions:

  - `printAllKeys()`  
  - `printAllValues()`  
  - `printAllItems()`
  
However, these functions did not contain any parameters.

A parameter is a variable that adds specific actions to a function. An **argument** is the value that is contained in the parameter variable. 

- The parameter is defined in the `def` statement of the function.

  - For example: `my_function(parameter_one, parameter_two)` passes two parameters to the function `my_function()`.

- **Note:** When we pass a direct string into a print statement, it is an argument. When we pass a variable, it is a parameter. 

    - For example: `print("this is an argument, paired with a " + parameter)`

#### Parameters Code Along

Open [Parameters.py](Activities/04-Parameters/Parameters.py) in VS Code to get an overview of parameter usage.

Close the file and create your own `my_parameters.py` script and follow along, adding the code blocks below to your script. 

1. Start by creating a function that takes in the parameter `name`. 

    ```python
    def printName(name):
       print("Oh! Hello " + name)
    ```

    - This code takes in the `name` variable and prints it in a string. 

2. We can use the same function and pass names in as arguments. 

    ```python
    printName("Mark")
    printName("Rose")
    printName("Denny")
    ```

    - The output will  print a string with each of these names inserted. You can save the script and run it at this point to verify. It should print:

        ```bash
        "Oh! Hello Mark"
        "Oh! Hello Rose"
        "Oh! Hello Denny"
        ```

3. Function parameters can include a default value. This means that if you call a function but do not include a specific argument, the default value will be assigned. All parameters with default values must come after the parameters without. 

    Let's create a function with an assigned variable and a default variable. 

    ```python
    def recordScore(name, score=0):
        print(name + "'s score is " + str(score))
    ```

    - We are taking in two parameters: `name` and `score`. If a parameter for `score` is not given, it will hold the default value of zero.

    - After we take in our parameters, we have another formatted `print` string to print a statement.

4. We can now call this function in a few ways. We can call it without giving it a score, or we can pass it a score. We can also pass it a variable that holds a score value or a name value. 

    - We can add the following code to our script:

        ```python
        recordScore("Jacob")
        recordScore("Ahmed", 20)
        recordScore("Steven", 15)
        ```

    - Or, we can add this: 

        ```python
        name = "Jacob"
        score = 30

        recordScore(name, score)
        ```

5. Save and run your script to see its output:

    ```bash
    $ python3 my_parameters.py
    Oh! Hello Mark
    Oh! Hello Rose
    Oh! Hello Denny
    Jacob's score is 0
    Ahmed's score is 20
    Steven's score is 15
     ```

---

### 05. Challenge: Functional Calculator 

In this challenge, you will make a command-line calculator application. The application will ask the user what kind of arithmetic operation they would like to perform. 

Open the unsolved file in VS Code: 

- [FunctionalCalculator.py](Activities/05-Functional-Calculator/Unsolved/FunctionalCalculator.py)
  
#### Instructions
  
In this challenge you are creating a command-line calculator application. When completed, the app should perform the following:

1. Ask the user what kind of arithmetic operation they would like to use.

2. Add two integers together if the user selects addition.

3. Subtract two integers from one another if the user selects subtraction.

4. Multiply two integers together if the user selects multiplication.

5. Divide two integers by one another if the user select division.

Each of the arithmetic operations should be contained within functions that take in two integers as parameters.

#### Walkthrough

Compare your script with a solved version: 

- [Solved: FunctionalCalculator.py](Activities/05-Functional-Calculator/Solved/FunctionalCalculator.py) 
 
Use the following walkthrough to review.

The script provides a basic outline of the code, along with an `addition()` function that takes in parameters `x` and `y`.

- `addition()` adds `x` and `y` and then prints a statement showing us the sum.


    ```python
    def addition(x,y):
       outcome = x+y
       print(str(x) + "+" + str(y) + "=" + str(outcome))
    ```


1. The majority of the challenge is creating our other functions, `subtraction()`, `multiplication()` and `division()`, before we call them in the final `while` loop.

    - All  the functions are defined with the same two parameters: `x` and `y`. These variables can be used multiple times since parameters only exist within the scope of a function. 

    - We can use the built-in math functions to create our new calculator functions. Notice that each function uses the same print statement:

    ```python
    def subtraction(x,y):
       outcome = x-y
       print(str(x) + "-" + str(y) + "=" + str(outcome))
    
    def multiplication(x,y):
       outcome = x*y
       print(str(x) + "*" + str(y) + "=" + str(outcome))

    def division(x,y):
       outcome = x/y
       print(str(x) + "/" + str(y) + "=" + str(outcome))
    ```

2.  Start our `while` loop by printing out a selection of options:

    ```python
    go_again = "y"

    while str(go_again) == "y":
        userChoice = int(input("What kind of calculation would you like to perform?\n[1]Addition\n[2]Subtraction\n[3]Multiplication\n[4]Division\nEnter Choice: "))
        print("-------------------------")
    ```

3. Add action to each selection option. First, we will use our `addition()` function:

    ```python
    if(userChoice == 1):
        firstNumber = int(input("What is the first number? "))
        secondNumber = int(input("What is the second number? "))

    # Call the addition function
        addition(firstNumber, secondNumber)
    ```

4. Add `elif` statements for each of the other functions:

    ```python
    elif(userChoice == 2):
        # Collect and store two numbers from the user
        firstNumber = int(input("What is the first number? "))
        secondNumber = int(input("What is the second number? "))
        # Call the subtraction function
        subtraction(firstNumber, secondNumber)

    elif(userChoice == 3):
        # Collect and store two numbers from the user
        firstNumber = int(input("What is the first number? "))
        secondNumber = int(input("What is the second number? "))
        # Call the multiplication function
        multiplication(firstNumber, secondNumber)

    elif(userChoice == 4):
        # Collect and store two numbers from the user
        firstNumber = int(input("What is the first number? "))
        secondNumber = int(input("What is the second number? "))
        # Call the division function
        division(firstNumber, secondNumber)
    ```

5. Add a catch-all output at the end of the `if` statement:
   
    ```python
    else:
        print("Not a specified option")
    ```

6.  Add user input to either repeat the loop or stop with a message:

    ```python
        go_again = input("Should we go again? (y)es or (no) >> ")

    print("Thank you for playing!")
    ```

    - Notice that the final print statement is outside of our loop, so it will only execute when the loop stops.

7. Run the final script to view its output:

    ```bash
    $ python3 FunctionalCalculator.py 
    What kind of calculation would you like to perform?
    [1]Addition
    [2]Subtraction
    [3]Multiplication
    [4]Division
    Enter Choice: 1
    -------------------------
    What is the first number? 5
    What is the second number? 6
    5+6=11
    Should we go again? (y)es or (no) >> y
    What kind of calculation would you like to perform?
    [1]Addition
    [2]Subtraction
    [3]Multiplication
    [4]Division
    Enter Choice: 3
    -------------------------
    What is the first number? 5
    What is the second number? 6
    5*6=30
    Should we go again? (y)es or (no) >> n
    Thank you for playing!
    ```

---

### 06. Returning Values

So far, we've passed parameters and values into functions. Once the function completes, we can also return those values, instead of just printing them. This can be done using the `return` keyword and  statements.

Open [ReturnStatements.py](Activities/06-Return/ReturnStatements.py) in VS Code to get an overview of return statements.

This script defines the `sum` function using a `return` statement: 

```python
def sum(a, b):
    return a + b
```

The value placed after `return` will be passed back to the main script when the `sum` function is called.

- For example: 

    ```python
    # use the 'return' keyword in a function
    def sum(a, b):
       return a + b

    result = sum(2, 3)
    print("The first sum is " + str(result))
    ```

- When a function containing a `return` statement is called, it is common to store the result within a variable so that the value can be referred to throughout the the application.

- In this example, the `result` variable holds the value returned by our `sum()` function, which is the integer `5`.

- Similarly, the next example stores a new result to a new variable:

    ```python
    result2 = sum(4, 6)
    ```

- The following example reminds us that we can also pass variables (parameters) into a function, instead of the direct arguments:

    ```python
    sumOfSums = sum(result, result2)
    print("The sum of sums is " + str(sumOfSums))
    ```

- Run the script to see its output:

    ```bash
    $ python3 ReturnStatements.py 
    The first sum is 5
    The second sum is 10
    The sum of sums is 15
    ```

---

### 07. Challenge: Validate Password 

In this challenge, you will create an application that checks whether or not a password entered by the user is of valid length.
 
Open the following file in VS Code: 

- [ValidatePassword.py](Activities/07-Validate-Password/Unsolved/validate_password.py)
 
#### Instructions
  
Using the script file provided, complete the following: 

1. Define a function called `validate_password` that accepts a string `password` parameter.

2. Inside the function, check if the password is longer than six characters. Return `True` if it is and return `False` if it is not.

3. Prompt the user to enter a password. Send this password to the `validate_password` function. Save the result of the function to a variable called `result`.

4. Print the value of `result` to the terminal.

**Hints:** 
- Like lists, strings can be looped through. However, in this case, the application is looping through each character in the string instead.

- The length of a string can be collected using the `len()` function.

#### Walkthrough

Compare your script to the solved version: 

- [Solved: ValidatePassword.py](Activities/07-Validate-Password/Solved/validate_password.py) 

Use the walkthrough to review the steps.

In this challenge, we are checking if a string has more than six characters.

1. First, the `validate_password` function needs to take in a string. Since this string is supposed to be a password, we will use the parameter variable `password`. 


    ```python
    def validate_password(password):
    ```

2. The `len()` function can check the length of a string. Therefore, `if (len(password) > 6)` will check whether or not the password entered by a user is greater than six characters in length. Let's add this to our function:

    ```python
    if (len(password) > 6):
        return True
    else:
        return False
    ```

    - This function can return boolean `True` or `False`. 


3. Take in a string and save it to a variable `passwordToCheck`:

    ```python
    passwordToCheck = input("Enter the password to check: ")
    ```

4. Now we can call our `validate_password()` function and pass it through the string we just collected:

    ```python
    result = validate_password(passwordToCheck)
    ```

5. We can print our result, which should give us `True` or `False`:

    ```python
    print(result)
    ```

6. Your final script should look similar to:

    ```python
    def validate_password(password):
        if (len(password) > 6):
            return True
        else:
            return False

    passwordToCheck = input("Enter the password to check: ")

    result = validate_password(passwordToCheck)

    print(result)
    ```

7. Run the script to see its output:

    ```bash
    $ python3 validate_password.py 
    Enter the password to check: password
    True

    $ python3 validate_password.py
    Enter the password to check: pass
    False
    ```

---

### 08. Challenge: User Creation

Building on the previous Validate Password challenge, you will now create a command-line application that allows users to create new accounts.

Open the unsolved file in VS Code: 
- [CreateUserFunctionsRefactored.py](Activities/08-User-Creation/Unsolved/CreateUserFunctionsRefactored.py)
 
#### Instructions

The application you create will allow users to create usernames, passwords, and email addresses for an account. Users will only be able to create accounts if their password meets the password length. It should also print out the account information to the terminal. 

Using the script file provided, create an application with the following features: 

1. A function called `collect_user_information` that will prompt the user for username, password, and email address. It should return this information in a list that contains those three values.

2. The above returned list should be passed into a function called `create_user` that checks if the password entered is valid.
            
4. If the password is valid, it will create a new dictionary for the user with the inputted information. The dictionary should have keys for username, password, and email with the associated values that the user entered. It should then print a message to the screen with this information.
      
5. If the password is not valid, it should print a message to the screen letting the user know that their password isn’t valid.

#### Walkthrough 

Compare your script with the provided solution file: 

- [Solved: CreateUserFunctionsRefactored.py](Activities/08-User-Creation/Solved/CreateUserFunctionsRefactored.py)

Use the following walkthrough to review the steps. 

The script provided a `validate_password()` function, the start of a `collect_user_information()` function, and a `create_user()` function.

1. The `collect_user_information()` function needs to collect the usernames, passwords, and email addresses from users. All the values can be stored within a list variable, in this case `user_info`, and we can return this list from the function. It looks like:

    ```python
    def collect_user_information():
        username = input("What's your username? ")
        email = input("What's your email? ")
        password = input("What's your password? ")

        user_info = [username, email, password]

        return user_info
    ```

     - Here we can see that we are using three `input()` functions assigned to different variables and then putting those variables into a list. At the end of the function, we return the list.
  
2. Complete the `create_user()` function. Inside the `create_user()` function, we can call the `validate_password()` function within an `if` statement:

    ```python
    def create_user(user_data):
        username = user_data[0]
        email = user_data[1]
        password = user_data[2]

        if validate_password(password):
            user = {
                "Username": username,
                "Email": email,
                "Password": password
            }
            for key, value in user.items():
                print("Your " + key + " is: " + value + ".") 
            return user
        else:
            print("Your password is too short, try again!"
    ```

     - This function is taking in the `user_data` list. In this case, the `user_data` variable that our `create_user()` function is written with is actually a different variable than the `user_data` list that is returned by the `collect_user_information()` function. We are giving them the same name to make it clear where our `user_data` list should be used.

3. At the top of this function, we separate the different username, email, and password data from this list by assigning them to new variables:

    ```python
        username = user_data[0]
        email = user_data[1]
        password = user_data[2]
    ```

4. The `if` statement returns `True` or `False`:


     ```python
     if validate_password(password):
     ```


5. We create the `user` dictionary and the `for` loop:

    ```python
    user = {
        "Username": username,
        "Email": email,
        "Password": password
    }

    for key, value in user.items():
        print("Your " + key + " is: " + value + ".") 
    return user
    ```

6. It is important to note that this function returns the `user` dictionary if the password is validated. If the password isn't validated, the `else` statement prints a message:

    ```python
    else:
        print("Your password is too short, try again!")
    ```

7. The final part of our script calls our functions:

    ```python
    user_data = collect_user_information()

    user = create_user(user_data)
    ```

    - The `collect_user_information()` function is called and the value it returns is saved to the variable `user_data`.

    - Then, we call the function `create_user()`, pass the `user_data` list, and save the return value of `create_user()` to a new `user` variable.

    - Note that this `user` variable is globally defined. The variable `user` that is returned by our `create_user()` function has a scope local to the `create_user()` function.


### 09. Reading Text Files

Up until now, we've used the  `input()` function to input external data into our Python applications. This function is useful when we need to collect only small amounts of data. However, it can be difficult and unwieldy for scripts and programs in which large collections of data would need to be entered into the command line. 

To solve this problem, we can use scripts that read  external files and collect the desired information. This saves us lots of time and makes our applications more robust. 

#### Reading the Diary Script Code Along

Open the following two files in VS Code:
- [Diary.txt](Activities/09-Reading-Files/Diary.txt) 
- [ReadingTextFiles.py](Activities/09-Reading-Files/ReadingTextFiles.py) 


`ReadingTextFiles.py` is a script file that we will use to read our `Diary.txt` file. To do this we will need to create a connection between the script file and the external file. 
  
We can create that connection using the built-in `open()` function.

- In the `open()` function,  the relative or absolute path to the file is provided as a parameter.
   
    ```python 
    diary_txt_file = open("Diary.txt","r")
    ``` 


    - `diary_txt_file =` is assigning the result of `open()` function to a variable.
    - `open()` is a function that opens a file.
    - `"Diary.txt"` is the file we are opening.
        - Since this file is in the same directory as  the script,  we do not need to give it a full path.
        - Be careful when creating relative paths. Navigation will start from the location of the script. 
    - `"r"` indicates that we will read the file. The `open()` function defaults to `r` for its second parameter if none is entered. 
   

The `open()` function returns a file object that we can save to a variable. 
- In this case, we are saving it to `diary_txt_file`. 
- Attempting to print this variable will only return some object data and will not provide any clarity about what the file contains.

To gather more context, we need to use the `file.read()` method. 
- This will return a string version of the file's contents. 
- The results of `.read()` can be assigned to another variable and then printed. This is the next part of our script:
   
    ```python
    diaryText = diary_txt_file.read()
    print(diaryText)
    ```

The connection to a file can be closed at any time using the `file.close()` method. 

- Python may not automatically close the file. If you write a program that opens a lot of files, it's important to close them. Keeping the files open risks using up your memory. 
  
    ```python
    diary_txt_file.close()
    ```

### 10. Challenge: Reading Rainbow

In this challenge, you will create a command-line application that asks the user for a color. If this color has an associated file, the script will open up the file and print its contents to the terminal.

Open the following script in VS Code: 

- [ReadingRainbow.py](Activities/10-Reading-Rainbow/Unsolved/ReadingRainbow.py)

- Extract the contents of `Starter.zip` and locate the `ReadingRainbow.py` file that was included. 
    - Use the comments in `ReadingRainbow.py` to help guide your work.

#### Instructions

Using the provided script, create an application that does the following:

1. Asks the user for a color and saves their response to a variable.

2. Checks to make sure that the color the user entered has an associated file.

3. If there is a matching file, creates a connection to this file, reads through its contents, and prints them to the terminal before closing the connection.

4. If there is no matching file, prints "No file associated with that color."

**Hints:**

- Look through the `Colors/` subfolder before creating the conditional to figure out which values you should be checking for.

- Create a connection to one specific file or folder path before trying to create a connection string that depends on the value the user entered.  Your connection should be to the `Colors/` subfolder. It should not consist of multiple connections to individual files.

#### Walkthrough

Compare your script to the solution file:

 - [Solved: ReadingRainbow.py](Activities/10-Reading-Rainbow/Solved/ReadingRainbow.py)

Use the following walkthrough to review the steps.

1.  Use an `input()` statement to ask the user for a color and save it to a variable:

    ```python
    color = input("What color would you like to look up? ")
    ```

2. Check that the color entered is one of the colors with an associated file in the `Colors` directory. There are a few different ways to set up the conditional:
    - We can create one large `if` statement that checks if the color entered matches any of the files, using `or` operators.
    - We can check each color individually using `if`, `elif`, and `else`.

    Neither option is technically better than the other, but the first method is more concise, so we'll use that one:

    ```python
    if (color == "red" or color == "orange" or color == "yellow" or color == "green" or color == "blue" or color == "violet"):
    ```

3. Use the `open()` function to create a connection to the file that the user enters. Since the files are in the `Colors` folder, the path should be `Colors/<Input>.txt`:

    ```python
    colorFile = open("Colors/" + color + ".txt")
    ```

    - The path to the file is constructed by referencing the `Colors/` subfolder, adding the color inputted by the user, and appending `.txt` to the end of the newly constructed path.

    - Remember: We don't need to use `"r"` because it is the default behavior of `open()`.

4. The application needs to read the text contained within `colorFile` using the `.read()` method. Then it needs to print the text:

    ```python
    colorText = colorFile.read()
    print(colorText)
    ```

5. Make sure to close the connection to `colorFile` after we are finished reading it:

    ```python
    colorFile.close()
    ```

6. If there is no file associated with the color entered, print a statement to the screen. This statement is the `else` part of our `if` statement:

    ```python
    else:
        print("Sorry! There is no associated file for that color.")
    ```

7. Run the script to see its output:

    ```bash
    $ python3 ReadingRainbow.py 
    What color would you like to look up? green
    Alligator
    Anaconda
    Apple
    Avocado
    Cactus
    Celery
    Hose
    Octopus
    Tree

    $ python3 ReadingRainbow.py
    What color would you like to look up? red
    Apple
    Barn
    Bricks
    Cardinals
    Cherries
    Fire Trucks

    $ python3 ReadingRainbow.py
    What color would you like to look up? maroon
    Sorry! There is no associated file for that color.
    ```

### 11. String Functions

Large blocks of text are not easy to work with. Their size makes it difficult to find and extract information. 

We can use the `string.split()` method to break down text into smaller chunks based on the string value passed into it as a parameter. 

- These chunks are then placed into a list so they can be more easily navigated through. 

- For example, `string.split(". ")` returns a list of strings in which each element was originally separated by a period followed by a space.

#### String Functions Script Code Along

Open [StringMethods.py](Activities/11-String-Methods/StringMethods.py) in Visual Studio Code for an overview of the `.split()` method.

- This script breaks up the `Diary.txt` file into smaller chunks.

Create a new script named `string_methods.py` and code along, adding the code blocks below to your script:

1. Open the `Diary.txt` file and use the `read` function to stringify the text:
   
    ```python
    diary_txt_file = open("Diary.txt","r")
    diaryText = diary_txt_file.read()
    ```


2. Use the `.split()` method on the `diaryText` string. Save the result to a new variable named `diary.split`: 
    ```python
    diarySplit = diaryText.split(" ")
    ```

3. Now that we have a list of words saved in `diarySplit`, we can print it like any list. Let's print a few words from our list: 
    
    ```python
    print(diarySplit[0])
    print(diarySplit[1])
    print(diarySplit[2])
    print(diarySplit[3])
    print("-----------"
    ```

    - Run the script to see its current output:

        ```python
        $ python3 string_methods.py 
        Today
        I
        am
        so
        -----------
        ```

4. The `string.find()` method is a simple tool we can use to find specific words or values within a string. 

    - `string.find()` determines if the substring passed into it as a parameter occurs anywhere in the text the method is being run on.

    - If the substring is found within the original text, it returns the index of the first occurrence. The value of the index returned is the character location where the substring begins. 

    - If the substring is not found within the original string, it returns a value of negative one (`-1`) .

    Add the `.find()` method to locate the words "malarkey" and "juice." We can first use it directly in a print statement:

    ```python
    print(diaryText.find("malarkey"))
    ```

    - Let's run our program at this point to see its current output:

        ```python
        $ python3 string_methods.py 
        Today
        I
        am
        so
        -----------
        209
        ```

    - We can see that the word "malarkey" is located at index `209`. Let's turn this into an `if` statement that prints a message _if_ "malarkey" is found. Add the following code to your script:

        ```python
        if diaryText.find("malarkey") > -1:
            print("Malarkey found!")
        ```

    - We are using `-1` instead of `0` because `0` is the first word in our text. Therefore, we want to make sure we include it in our search.

5. Next, let's  check for the word "juice":

     ```python
    if diaryText.find("juice") > -1:
        print("Juice found")
    ```

6. Print a line at the end of the output and close the TXT file.:
    ```python
    print("-----------")

    diary_txt_file.close()
    ```

7. Your final script should look similar to:

    ```python
    diary_txt_file = open("Diary.txt","r")
    diaryText = diary_txt_file.read()

    diarySplit = diaryText.split(" ")

    print(diarySplit[0])
    print(diarySplit[1])
    print(diarySplit[2])
    print(diarySplit[3])
    print("-----------")

    print(diaryText.find("malarkey"))

    if diaryText.find("malarkey") > -1:
        print("Malarkey found!")

    if diaryText.find("juice") > -1:
        print("Juice found")

    print("-----------")

    diary_txt_file.close()
    ```

8. Run the final script to see its output:

    ```bash
    $ python3 string_methods.py 
    Today
    I
    am
    so
    -----------
    209
    Malarkey found!
    -----------
    ```

    - We can see that the word "juice" was not found.

### 12. Challenge: Word Search

In this challenge, you will create a command-line application that looks at a specific file and asks the user to enter a word. The application will search through the file, find any instances of the word, and print how many times the word was found.

Open the following script in VS Code:

- [WordSearch.py](Activities/12-Word-Search/Unsolved/WordSearch.py) 

#### Instructions

Given the WordSearch.py file and the `Monologue.txt` file, create a  function called `wordSearch()` that will take in a string as a parameter and carry out the following tasks:

1. Open and read the text contained within `Monologue.txt`.

2. Search through the text to determine if the string passed into `wordSearch()` can be found.

3. Print out how many times the string passed can be found within the original text.

**Hints:**

- When `string.split()` is used to discover how many instances of a string appear within a block of text, the length of the list returned is always one more than it should be.

- Remember that you have to call a function in order to use it. Defining a function is not enough. 

#### Walkthrough

Compare your script with the following solution file: 

- [Solved: WordSearch.py](Activities/12-Word-Search/Solved/WordSearch.py)

Use the walkthrough to review the steps.

1. Create a function that takes in a word and then searches for the word within the text. We will call our function `wordSearch()`:

    ```python
    def wordSearch(word):
    ```

2. Open the `Monologue.txt` file from inside the function, read the text, and save it to a variable for later use. Any references to the file must be made from within the function or they will be considered out of scope.

    ```python
    monologueFile = open("Monologue.txt")
    monologueText = monologueFile.read()
    ```

3. Note that `string.find()` is not perfect. It cannote determine whether the substring the user is looking for is an independent word or just a couple of characters contained within a word. This means that if we search for `he` in the string, `hello` will come back as true.

    - Therefore, when searching for a word, we have to create a new string with blank spaces on each side of the word. This will ensure that the word `carmen` does not return if we search for `car`. 

    - Adding spaces does have drawbacks. For example, the first word in the monologue has no space before it and therefore would not be found. Also, words at the ends of sentences have periods after them and would not be found either. While this solution is not perfect, it will prevent false positives. 


    ```python
    wordWithSpace = " " + word + " "
    ```

4. Now we can create an `if` statement that searches for the word as the conditional. If the word is found, it will count how many times it was found and print the number. If no instances of the word are found, it will print a statement saying the word is not in the text.

    ```python
    if (monologueText.find(wordWithSpace) > -1):
        countList = monologueText.split(wordWithSpace)
        print("The word" + wordWithSpace + " can be found " + str(len(countList) - 1) + " times")
    else:
        print("The word" + wordWithSpace + " is not in the text")
    ```


     - `if (monologueText.find(wordWithSpace) > -1):` starts the `if` statement and returns true if the word is found in any index.
     - `countList = monologueText.split(wordWithSpace)` splits the text by the word we are looking for. Each time the word is found, the text is split and added to a list. We can then count the number of chunks that comprise the list and subtract one to get the number of words. 
        - We subtract one because a split will always create two parts for the first match it finds, and one more for each additional match. 
     - `print("The word" + wordWithSpace + "can be found " + str(len(countList) - 1) + " times")` prints the statement if the word is found.
     - `else` executes the following code when our conditional returns false. 
     - `print("The word" + wordWithSpace + "is not in the text")` prints if the word is not found. 

5. Now we can call our completed function finished. Start by collecting a word from the user and storing it in a variable. Then, call the function and pass it the variable:

    ```python
    wordToSearch = input("Please enter a word to search for: ")
    wordSearch(wordToSearch)
    ```

6. The final script (without comments) looks like this:

    ```python
    def wordSearch(word):
        monologueFile = open("Monologue.txt")
        monologueText = monologueFile.read()
        wordWithSpace = " " + word + " "

        if (monologueText.find(wordWithSpace) > -1):
            countList = monologueText.split(wordWithSpace)
            print("The word" + wordWithSpace + "can be found " + str(len(countList) - 1) + " times")
        else:
            print("The word" + wordWithSpace + "is not in the text")

    wordToSearch = input("Please enter a word to search for: ")
    wordSearch(wordToSearch)
    ```

7. Run the script to view its output:

    ```bash
    $ python3 WordSearch.py 
    Please enter a word to search for: blue
    The word blue is not in the text

    $ python3 WordSearch.py
    Please enter a word to search for: Juice
    The word Juice is not in the text

    $ python3 WordSearch.py
    Please enter a word to search for: Malarkey
    The word Malarkey is not in the text

    $ python3 WordSearch.py
    Please enter a word to search for: The
    The word The is not in the text

    $ python3 WordSearch.py
    Please enter a word to search for: the
    The word the can be found 11 times
    ```

-------

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.   