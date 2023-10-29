""" 
LAMBDA FUNCTION IN PYTHON
    > a lambda function is a small anonymous function without a name. 
    > It is defined using the lambda keyword and has the following syntax:
    
    lambda arguments: expression

    > Lambda functions are often used in situations where a small function is required for a short period of time. 
    > They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.
    > lambda function is anonymous, as it does not have a name.
    > Lambda functions can have multiple arguments, just like regular functions.
"""

square = lambda x: x*x
name = lambda x,y: "I'm " + x + " and she is " + y +"."
print(square(5))
print(name("Prince", "Riya"))

# with additional print statement
mul = lambda x, y: print(f'{x} * {y} = {x * y}')
mul(4,5)

# callback function
def apple(fx, value):
    return 10 + fx(value)
print(apple(square, 10))