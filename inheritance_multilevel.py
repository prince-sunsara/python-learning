""" 
MULTILEVEL INHERITANCE IN PYTHON:
    > Multilevel inheritance is a type of inheritance in oop where a derived class inherits from another derived class.
    > his type of inheritance allows you to build a hierarchy of classes where one class builds upon another, leading to a more specialized class.
    > In Python, multilevel inheritance is achieved by using the class hierarchy.
    > Syntax: 
        class BaseClass:
            # Base class code
            
        class DerivedClass1(BaseClass):
            # Derived class 1 code
            
        class DerivedClass2(DerivedClass1):
            # Derived class 2 code
"""
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class LabradorDog(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Labrador")
        self.color = color
    
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

d = LabradorDog("Taffi", "Black & White")
d.show_details()

""" 
    > This is a powerful feature of multilevel inheritance, as it allows you to create more complex and intricate classes by building upon existing ones.
    > Another important aspect of multilevel inheritance is that it allows you to reuse code and avoid repeating the same logic multiple times
    >  This can lead to better maintainability and readability of your code, as you can abstract away complex logic into base classes and build upon them.
"""