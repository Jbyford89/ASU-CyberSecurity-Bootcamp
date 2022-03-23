# Cheat Sheet - Python Day 1

## Key Terms

- **Python**: Python is a high-level, general purpose programming language used for a variety of applications. Python `files` have the format `filename.py` 
  
  - Example: `HelloWorld.py`

- **Program**: A program is a series of **instructions** or **statements** to perform specific tasks.  

  - Example: 

    ```bash 
    # My First Python Program
        print ("hello world")
    ``` 

- **Comment**: A comment explains blocks of code in a Python program.  Comments start with the `#` character.

  - Example: 
  
    ```bash 
        # My First Python Program
    ```

- **Data**: Data is information stored in a computer. 
  - Example:  `5`, `Hello World`

- **Variable**: Variables are the means by which we store and reference data.

  - Example: In this example `name` is a **variable** used to store the value `Tony`.

    ```bash 
    # Create a variable called name and assign it the value 'Tony'
        name = "Tony"
    ``` 

- **Assignment Statement**: An assignment statement is used to **store the value** of a variable. 
    * An assignment statement has the syntax: `<variable><assignment operator><value>`


   - Example: Using our example we use an **assigment statement** to store the **value** `Tony` in the **variable** `name`.
 
```bash 
# Create a variable called name and assign it the value 'Tony'
# ================================================================
    name = "Tony"
``` 

### Variable Types

- **String Variable**: A string variable is any collection of characters surrounded by a single or double quotation mark. Strings can contain numbers within them but these numbers are seen as characters without any numeric value.

  - Example:  In our example **Tony** is a `string` variable.

    ```bash 
    # Variable Assignment
    # ===================
    # String
    name = "Tony"
    ```

- **Integer Variable**: An integer variable stores a whole number (e.g., 10, -1000). Integers can be positive or negative and any length.

  - Example:  In this example we assign the value **10** to  `int_variable`.

    ```bash 
    # Variable Assignment
    # ===================
    # Integers
    int_variable = 10
    ```

- **Float Variable**: A float variable stores numbers with a decimal point.  They are different from integers in that integers have to be whole numbers while floats can contain decimals within them.

  - Example:  In this example we assign the value **1.25** to `float_variable`.

    ```bash 
    # Variable Assignment
    # ===================
    # Floats
    float_variable = 1.25
    ```

- **Boolean Variable**: A boolean variable has the value `True` or `False`.

  - Example:  In this example we assign the value **True** to `boolean_variable`.

    ```bash 
    # Variable Assignment
    # ===================
    # Booleans
    boolean_variable = True
    ```

- **List Variable**: Lists are collections of data. These collections can be made up of strings, numbers, Booleans and contain related data. Items in a collection are surrounded by **[ ]**.

  - Example:

    ```bash 
    # Create a list of actor's names
    # ==============================
    actors = ["Tom Cruise", "Angelina Jolie", "Kristen Steward", "Denzel Washington"]
    ```

- **Dictionary Variable**: A dictionary stores **key-value pairings**.  The `key` is a string that can be referenced in order to **collect the value** that is associated with it. The key-value pairs are denoted by **{key : value}**.

  - **Examples**:

    ```bash 
    # A dictionary entry for an actor
    # =======================================
    actor = { "name" : "Tom Cruise"}
    ```

    ```bash 
    # A dictionary with multiple pairs of information
    # ===============================================
    actress = {
      "name": "Angelina Jolie",
      "genre": "Action",
      "nationality": "United States"
      }
    ```

    ```bash 
    # A dictionary can contain multiple types of information
    # ========================================================
    another_actor = {
        "name": "Sylvester Stallone",
        "age": 78,
        "married": True,
        "best movies": [
          "Rocky",
          "Rocky 2",
          "Rocky 3"
          ]
        }
    ```

    ```bash 
    # A dictionary can even contain another dictionary
    # ========================================================
    film = {"title": "Interstellar",
            "revenues": {
              "United States": $360m, 
              "China": $250m, 
              "United Kingdom": $73m
              }
            }
    ```

### Operators

- **Assignment Operators**: Assignment operators are used to assign a **value** to a **variable**.

  - Example:  In this example we use the assigment operator `=` to assign the `value` **Tony** to `variable` **name**.

    ```bash 
    # Create a variable called name and assign it the value 'Tony'
    # ================================================================
        name = "Tony"
    ``` 

- **Arithmetic Operators**: These operators perform arithmetic operations.

  - Example:  In this example we use the **multiplication** operator `*` and print the result.

    ```bash 
    # Multiply two numbers and print the result
    # =========================================
        print (5 * 10)
    ``` 

- **Comparison Operators**: These operators are used to compare two values.

  - Example:  In this example we use the **greater than** operator `>` and print the result.

    ```bash 
    # Is 5 greater than 10?
    # ========================
        print (5 > 10)
    ``` 

- **Logical Operators**: These operators are used to combine statements.

  - Example:  In this example we use the **and** operator to see if **both** statements are true.

    ```bash 
    # Is this statement true?
    # ========================
        x = 5
        print (x > 2 and x < 10 )
    ``` 

- **String Concatenation**: This operation provides a way to **combine** strings. It uses the `+` operator.

  - Example:  In this example we combine the strings **"Hello"** and **"World"** and assign it to the string `hello`.

    ```bash 
    # String Concatenation
    # ========================
        hello = "Hello" + "World"
        print (hello)
    ``` 

- **String Conversion**: This operation provides a way to convert a variable to a `string` type and uses the `str()` function.

  - Example: In this example we convert the integer variable **age** to a string variable.

    ```bash 
    # String Conversion and Concatenation
    # ===================================
        age = 27
        words = "I am currently "
        completeSentence = words + str(age)
        print (ompleteSentence)
    ``` 

## Key Commands

### Python Functions        

#### print () Print lines to the console

```bash 
    print ("hello world")
```

#### input () Get user input

```bash 
    name = input ("What is your name? ")
    print ("Hello" + name)
```

#### str() String conversion
```bash
    age = 27
    words = "I am currently "
    completeSentence = words + str(age)
```
-------

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.  