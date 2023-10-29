""" 
HYBRID INHERITANCE
    > Hybrid inheritance is a combination of multiple inheritance and single inheritance in oop.
    > it is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and single inheritance is used to inherit the properties of the derived class into a sub-derived class.
    > syntax:
        class BaseClass1:
        # attributes and methods

        class BaseClass2:
        # attributes and methods

        class DerivedClass(BaseClass1, BaseClass2):
        # attributes and methods
"""
class BaseClass:
    pass

class DerivedClass1(BaseClass):
    pass

class DerivedClass2(BaseClass):
    pass

class DerivedClass1(DerivedClass1,DerivedClass2):
    pass

""" 
HIERARCHICAL INHERITANCE
    > Hierarchical Inheritance is a type of inheritance in oop where multiple subclasses inherit from a single base class.
    > in other words, a single base class acts as a parent class for multiple subclasees.
    > this is a way of establishing relationship between classes in a hierarchical manner.
"""
class Animal:
    def __init__(self, name):
        self.name = name
        
    def show(self):
        print("Name:", self.name)
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def show(self):
        Animal.show(self)
        print("Species: Dog")
        print("Breed:", self.breed)

class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def show(self):
        Animal.show(self)
        print("Species: Cat")
        print("Color:", self.color)
        
dog = Dog("Viskey", "Golden Retriever")
dog.show()
cat = Cat("Mini", "Black")
cat.show()