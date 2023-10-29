""" 
CUNSTRUCTORS:
    > special method in a class to create and initialize an object of a class.
    > it invoked automatically when an object of a class is created.
    > A constructor is a unique function that gets called automatically when an object is created of a class.
    > The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.
    > init is one of the reserved functions in Python. In Object Oriented Programming, it is known as a constructor.
    
    > Types of Constructors in Python
        1. Parameterized Constructor
            > When the constructor accepts arguments along with self, it is known as parameterized constructor.
            def __init__(self, animal, group):

        2. Default Constructor
            > When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.
            def __init__(self):
"""

# dunder method : def __init__(self)
class Person:
    # constructor"
    def __init__(self, n, o):
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is {self.occ}")
a = Person("Prince", "Developer")
b = Person("Radhe", "HR")
a.info()
b.info()