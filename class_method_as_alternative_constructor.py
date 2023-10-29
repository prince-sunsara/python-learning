""" 
CLASS METHODS AS ALTERNATIVE CONSTRUCTORS:
    > In oop, the term 'constructor' refers to a special type of method that is automatically executed when an object is created from a class.
    > purpose of constructor is to initialize the object's attributes, allowing the object to be fully functional and ready.
    > a class method belongs to the class rather than to an instance of the class. one of the common use case for class methods as alternative constructor.
    > When you want to create an object from data that is stored in different format, such as a string or a dictinary.
"""
class Employee:
    def __init__(self, n, s):
        self.name = n
        self.salary = s
    
    @classmethod
    def from_string(cls, string):
        name, salary = string.split(",")
        return cls(name, int(salary))
    
e1=Employee.from_string("Raj,50")
print(e1.name)
print(e1.salary)