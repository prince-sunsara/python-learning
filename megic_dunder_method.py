""" 
MAGIC/DUNDER METHODS IN PYTHON:
    > These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manupulate objects and their behaviour.
    > Magic methods are also known as "dunder" from the double underscores surrounding their names, are powerful tools to customize the behavior of your classes.
    > they are used to impliment special methods such as the addition, subtraction, and comparison operators, as well as some more advanced techniques like description and properties.
"""

""" 
__INIT__ METHOD
    > the init method is a special method that is automatically invoked when you create a new instance of a class.
    > This method is responsible for setting up the object's initial state, and it is where you would typically define any instance variables that you need.
    > also call as 'counstructor'.
"""
# class Employee:
#     def __init__(self, name):
#         self.name = name
# e = Employee("prince")

""" 
__STR__ & __REPR__ METHODS
    > the str and repr methods are both used to conver an object to a string representation.
    > The str method is used when you want to print out an object
    > The repr method is used when you want to get a string representation of an object that can be used to recreate the object.
"""
# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"The name of the employee is {self.name} (str)"

#     def __repr__(self):
#         return f"The name of the employee is {self.name} (repr)"
    
# e = Employee("prince")
# # print(e)
# print(str(e))
# print(repr(e))

""" 
__LEN__ METHOD:
    > The len method is used to get the length of an object.
    > this is useful when you want to be able to find the size of a data structure, such as a list or library
"""
# class Employee:
#     def __init__(self, name):
#         self.name = name
    
#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i += 1
#         return i
# e = Employee("prince")
# # print(len(e))
# print(e)

""" 
__CALL__ METHOD
    > The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called.
    > This is an incredible powerful tool that allows you to create objects that behaves like functions.
"""