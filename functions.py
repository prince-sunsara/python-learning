"""
function:
block of code that perform a specific task whenever it is called

> built-in functino
    --> functions which are defined and pre-coded
    --> eg. min(), max(), range(), type()

> user-defined function
    --> we can create functions to perform specific tasks as per our needs.
    --> created with keyword 'def'
"""

def add(a, b):
    print(a + b)

def greater(a,b):
    pass            # pass gives you permission to write your code when you want

add(1,2)

"""
Arguments:

> default
> keyword
> variable length
> required
"""
def name(fname, mname, lname = "hub"):
    print("Hello all,", fname, mname, lname)

name("prince", "nareshbhai", "sunsara") # default arguments
name(fname="sunsara", mname="prince", lname="nareshbhai") # keyword argument
name("radhe", "radhe") # required argument(je default na hot eni must aapvi pde)

# variable length: access args as dictionary or tuple
def average(*numbers): 
    # print(numbers)  # (10, 20)
    # print(type(numbers))    # <class 'tuple'>
    sum = 0
    for i in numbers:
        sum = sum+i
    print("average is ", sum/len(numbers))

def averages(**numbers):
    # print(numbers)  # {'a': 10, 'b': 20, 'c': 30}
    # print(type(numbers)) # <class 'dict'>
    for i in numbers:
        print(i)
    
average(10,20)
averages(a=10,b=20,c=30)
