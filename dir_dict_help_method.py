"""
DIR(), __DICT__ and HELP() METHODS:
    > dir(), __dict__() and help() make it easy for us to understand how classes resolve various functions and executes code.
    >  In Python, there are three built-in functions that are commonly used to get information about objects: dir(), dict, and help().
"""

""" 
THE DIR() METHOD():
    > The dir() function returns a list of all the attributes and methods(including dunder methods) available for an object.
    > It is a useful tool for discovering what you can do with an object.
"""
# x = [1,2,3]
# print(dir(x))

""" 
THE __DICT__ ATTRIBUTE
    > the __dict__ attribute returns a dictionary representation of an object's attributes.
    > It is useful tool for introspection.
"""
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p = Person("prince", 20)
# print(p.__dict__)

""" 
THE HELP() METHOD:
    > The help() function is used to get help documentation for an object, including description of its attributes and methods.
"""
help(str)