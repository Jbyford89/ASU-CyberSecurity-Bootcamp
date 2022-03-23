# use the 'return' keyword in a function
def sum(a, b):
    return a + b

# assign the function call to a variable to use the value later
result = sum(2, 3)
print("The first sum is " + str(result))

result2 = sum(4, 6)
print("The second sum is " + str(result2))

sumOfSums = sum(result, result2)
print("The sum of sums is " + str(sumOfSums))