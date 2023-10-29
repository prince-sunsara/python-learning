""" 
INHERITANCE IN PYTHON:
    > When a classs derives from anohter class it calls inheritance.
    > The child class will inherit all the public  and protected properties and method from the parent class.
    > In addition, it can have its own properties and methods,this is called as inheritance.

    SYNTAX
    
    class BaseClass:
        Body of base class
    class DerivedClass(BaseClass):
        Body of derived class
    
    > Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.
    
    TYPES OF INHERITANCE:
        > Single inheritance
        > Multiple inheritance
        > Multilevel inheritance
        > Multilevel inheritance
        > Hybrid Inheritance
"""

class ParentClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def details(self):
        print(f"My name is {self.name} and I'm {self.age} year old")
        
class ChildClass(ParentClass):
        def showLanguage(self):
            print("This is child class")

    
p = ParentClass("Naresh", 51)
p.details()

q = ChildClass("Radhe", 19)
q.details()
