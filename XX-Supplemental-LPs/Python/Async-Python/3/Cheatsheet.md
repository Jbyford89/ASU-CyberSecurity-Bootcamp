## Python Day 2 Cheat Sheet: 

### Key Terms

- **Function**: A function is a block of organized, reusable code that can be used to perform a single action multiple times. Python comes pre-packaged with functions such as `print()`and `input()`. 

    
  ```bash 
  print("Hi, Alice.")      
  ``` 

- **Function Definition**: The `def` keyword is used to define a **user-defined** function. The `function name` is required. The code to run is *indented* in the function block. A function must be defined *before* you use it in a program.

  ```bash 
  def <required-function-name>(<optional-function-parameters>)<:>
      <indented statement> 
      <indented statement>
      <.....>
      <optional return statement>        
  ```         
  - **Example**: 

    ```bash 
    # Creating a new user-defined function called printHello()
    # This function does not have parameters or return a value
    def printHello():

      # This indented code will be run any time printHello() is called in the application
      print("Hello User!")
      print("You have just defined and called your first function!")
      print("Great job!")
      ```

- **Function Call**: Once you have defined a function the code can only be executed when you **call the function**  using the **function-name**. 

  ```bash  
  # A function must be executed in order for the code it contains to be run
  printHello()
  ``` 

- **Function Parameter**:  Functions can have `parameters`. Parameters are values that you provide to functions so that the function can perform actions using those values. Functions can have one or multiple parameters or a default value.


  ```bash  
  # Defining a function and giving it the parameter of "name"
  def printName(name):
      print("Oh! Hello " + name)
  ```

- **Function Argument**:  `Arguments` are the values you pass to a function when it is called. They are placed within the parentheses `( )`.
       

  ```bash  
  # Now any string value can be passed as an "argument" to the function within the parentheses
  printName("Mark")
  printName("Rose")
  printName("Denny")  
  ``` 

- **Return Statement**:  Functions can return values to the main script.  We do this by writing a `return statement` using the `return` keyword. The `return statement` indicates that once the function completes we are returning a value.


  ```bash  
  # use the "return" keyword in a function to return the sum of a + b
  def sum(a, b):
      return a + b)  
  ``` 

- **Scope**: The *scope* of a variable refers to the places that the application can see/access a specific variable.  The scope of a variable can be **local** or **global**.

  - **Example**:  See the following sections.

- **Global Scope**: Variables defined *outside* a function have **global** scope. They **can** be accessed from outside of the function.



  ```bash 
  # This variable is defined at the top level of the application
  # This means that its scope is "global" and it can be referenced anywhere
  global_variable = "I CAN GO ANYWHERE!"

  # Creating a function that prints to the console
  def printPhrases():
      print("Printing global variable within the function: " + global_variable)

  # Calling the function so as to run the code it contains
  printPhrases()

  print("----------")

  # Printing `global_variable` still works since it exists across the entire application
  print("Printing global variable outside the function: " + global_variable)   
  ``` 

- **Local Scope**: Variables defined *inside* a function have **local** scope. They **can not** be accessed from outside of the function.


  ```bash 
  # Creating a function that prints to the console
  def printPhrases():

    # This variable is defined within a function
    # This means that it can only be referenced within this function
    local_variable = "I ONLY EXIST IN THIS FUNCTION"

    print("Printing local variable within the function: " + local_variable)

  # Trying to print `local_variable` outside of the function returns an error
  print("Printing local variable outside the function: " + local_variable)     
  ``` 

## Key Python Function Commands

### User-defined Functions

#### Define a function without parameters.

```bash 
# Creating a new user-defined function called printHello()
# The function does not have parameters
def printHello():

  # This indented code will be run any time printHello() is called later in the application
  print("Hello World")
  print("You have just defined and called your first function!")
  print("Great job!")
  ```

#### Define a function with one parameter.

```bash 
# Defining a function and giving it the parameter of "name"
# "name" is a temporary variable that only exists within the scope of this function
def printName(name):
    print("Oh! Hello " + name)
```

#### Define a function with a parameter and a default value.

```bash
# Functions can be given multiple parameters
# Parameters can also be provided with default values
def recordScore(name, score=0):
  # The score that is printed out will default to 0 if none is provided
  print(name + "'s score is " + str(score)
```

#### Define a function that has a return value.

```bash
# use the "return" keyword in a function to return the sum of a + B
def sum(a, b):
    return a + b) 
``` 

### Calling Functions

#### Call pre-defined functions.

```bash
# Get input from the terminal and print
name = input("What is your name? ") 
print("Oh! Hello: " + name)
``` 

#### Call a user-defined function "without" arguments.

```bash 
def printHello():
  # This indented code will be run any time printHello() is called in the application.
  print("Hello User!")
  print("You have just defined and called your first function!")
  print("Great job!")

# A function must be executed in order for the code it contains to be run.
printHello()  
```

#### Call a user-defined function "with" an argument.

```bash 
def printName(name):
  # This indented code will be run any time printName() is called in the application.
  print("Oh! Hello: " + name) 

  # Now call printName() passing a name.
printName("Mark")
printName("Rose")
printName("Denny") 
```

#### Call a user-defined function with "arguments" and using a "default value".

```bash 
def recordScore(name, score=0):
  # The score that is printed out will default to 0 if none is provided
  print(name + "'s score is " + str(score)

 # Now call recordScore() passing a name and a score. Jacob will have the 'default score = 0'.
recordScore("Jacob")
recordScore("Ahmed", 20)
recordScore("Steven", 15)
```  

-------

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.   