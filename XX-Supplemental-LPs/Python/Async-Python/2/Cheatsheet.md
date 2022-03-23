## Python Day 1 Cheat Sheet: Python Day 2

### Key Terms

- **Conditional Statement**: A conditional statement tests a certain condition and based on the outcome runs a block of code if the condition is met. 



    ```bash 
    if (name == "Alice"):
        print("Hi, Alice.")      
    ``` 

- **for loop Statement**: The **for** loop allows you to run a block of code multiple times.  



    ```bash 
    # Start with a list
    vegetables = ["Carrots", "Peas", "Lettuce", "Tomatoes"]

    # Loop through each item of the list
    for vegetable in vegetables:
        print("I love " + vegetable)
    ``` 

- **while Statement**: The **while** loop runs a block of code *while a condition* is True.  


    ```bash 
    i = 0

    while i < 5:
        print(i) 
        i = i + 1   
    ``` 

- **enumerate**: The **enumerate** function allows you to iterate through a list while keeping track of where you are (index) in the list.



    ```bash 
    # The enumerate function allows programmers to loop through a list and create a counter
    # to reference the current iteration of the loop that they are on.

    hobbies = ["Rock Climbing", "Bug Collecting", "Cooking", "Knitting", "Writing"]

    for index, hobby in enumerate(hobbies):
        print(hobby + " is my #" + index + " hobby")    
    ``` 

### Operators

- **==** Operator: The **equals** `==` operator is used to test if two values are equal. It should not be confused with the `=` assignment operator. 

    ```bash 
    x = 1
    y = 10

    # Evaluates to True if the two values are equal
    if (x == 1):
        print("x is equal to 1")
    ``` 

- **!=** Operator: The **not equal** `!=` operator is used to test if two values are not equal. 


    ```bash 
    x = 1
    y = 10

    # Evaluates to True if the two values are NOT equal to each other
    if (y != 1):
        print("y is not equal to 1")
    ``` 

- **<** Operator: The **less than** `<` operator is used to check if one value is less than another value. 



    ```bash 
    x = 1
    y = 10

    # Checks if one value is less than another value
    if (x < y):
        print("x is less than y")
    ```

- **>** Operator: The **greater than** `>` operator is used to check if one value is greater than another value. 


    ```bash 
    x = 1
    y = 10

    # Checks that one value is greater than another value
    if (y > x):
        print("y is greater than x")
    ``` 

- **>=** Operator: The **greater than or equal to** `>=` operator is used to check if one value is greater or equal to another value. 

    ```bash 
    x = 1
    y = 10

    # Checks that a value is greater than or equal to another value
    if (x >= 1):
        print("x is greater than or equal to 1")
    ```

- **<=** Operator: The **greater than or equal to** `<=` operator is used to check if one value is less or equal to another value. 

    ```bash 
    x = 1
    y = 10
        
    # Checks that a value is less than or equal to another value
    if (x <= y):
        print("x is less than or equal to y")
    ```
 

## Key Commands 

### Simple Conditional Statements

#### If statement

```bash 
x = 1
y = 10
   
# Checks that a value is less than or equal to another value
if (x >= 1):
    print("x is greater than or equal to 1")
```

#### If - Else statement

```bash 
# The else block of code will only ever run when the if statement is False
if (x > 5):
    print("x is large")
else:
    print("x is small")
```

#### If-Elif-Else statement

```bash 
# The elif statement will run when the if statement returns a False but its own condition returns a True
# The else statement will run when both the if and elif (else if) conditions return as False
if (y < 5):
    print("y is less than 5")
elif (y == 5):
    print("y is lequal to 5")
else:
    print("y is greater than 5")
```

### Complex Conditional Statements

#### Using the 'and' Operator

```bash 
# Checks that both conditions are met using "and"
if (x == 1 and y == 10):
  print("Both values returned true")
```

#### Using the 'or' Operator

```bash 
# Checks if either of two conditions are met using "or"
if (x < 45 or y < 5):
  print("One or more of the statements were true")
```

#### Using 'nested' if statements

```bash 
# Nested if statements allow for more specific conditional pathways
if (x < 10):
  if (y < 5):
      print("x is less than 10 and y is less than 5")
  elif (y == 5):
      print("x is less than 10 and y is equal to 5")
  else:
      print("x is less than 10 and y is greater than 5")
```

#### Using the 'in' keyword

```bash 
# Checking whether a value is inside of a list using the `in` keyword
if (x in [1,2,3,4,5,6,7]):
  print("The value of x was inside of the list")
else:
  print("The value of x was not inside of the list")
```

### Looping Statements

#### for loop

```bash 
# Start with a list
vegetables = ["Carrots", "Peas", "Lettuce", "Tomatoes"]

# Loop through each item of the List
for vegetable in vegetables:
    print ("I love " + vegetable)
``` 

#### 'nested' for loop

```bash 
# A list of five letters
letter_list = ["B", "I", "N", "G", "O"]
# A list of 20 numbers
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# The first loop moves through all the letters in the letter list
for letter in letter_list:

  # The second loop moves through all the numbers in the number list
  for number in numbers_list:

    # Print out the unique letter/number combination
    print(letter + str(number))
``` 

#### range function

```bash 
# range(start, stop) allows you to loop through a range of numbers
# start is the starting value (inclusive), stop is the end value (not inclusive)
hobbies = ["Rock Climbing", "Bug Collecting", "Cooking", "Knitting", "Writing"]

for x in range (2,5):
    print(x)    
    # can reference element in list at index x
    print(hobbies[x])
```

#### enumerate function

```bash 
# The enumerate function allows programmers to loop through a list and create a counter
# to reference the current iteration of the loop that they are on.
# index is an integer which points to the current iteration of the loop
# hobby holds the value of the current element in the hobbie list.
for index, hobby in enumerate(hobbies):
    print(hobby + " is my #" + index + " hobby") 

# The enumerate function also allows programmers to choose what number
# to start counting from.  This means they can count from 1 instead of 0 
# if they so desire.
for index, hobby in enumerate(hobbies, start=1):
    print(hobby + " is my #" + index + " hobby")            
```

#### while loop

```bash 
i = 0

while i < 5:
    print(i) 
    i = i +1   
``` 

-------

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.   
