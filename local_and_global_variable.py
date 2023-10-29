"""
VARIABLES
    > A variable is a named location in memory that stores a value. 
    > we can assign values to variables using the assignment operator =.

LOCAL VARIABLES
    > A local variable is a variable that is defined within a function and is only accessible within that function. 
    > It is created when the function is called and is destroyed when the function returns.
    
GLOBAL VARIABLES
    > On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any function in your code.
"""

# x = 10 # global variable

# def my_function():
#   y = 5 # local variable
#   print(y)

# my_function()
# print(x)
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function


"""
THE GLOBAL KEYWORD
    > The global keyword is used to declare that a variable is a global variable and should be accessed from the global scope.
"""
# x = 10 # global variable

# def my_function():
#   global x
#   x = 5 # this will change the value of the global variable x
#   y = 5 # local variable

# my_function()
# print(x) # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function

