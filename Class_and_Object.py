"""
CLASSES IN PYTHON
    > A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). 
    > The user-defined objects are created using the class keyword.
"""
class Details:
    name= "Prince"
    age= 20
    def info(self):
        print(f"{self.name} is a {self.age} year old.")

""" 
CREATING AN OBJECT:
    > Object is the instance of the class used to access the properties of the class.
"""
d = Details()
print(d.name, d.age)

d.name = "Radhe"
d.age = 18
print(d.name, d.age)

"""
SELF PARAMETER:
    > Self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    > It must be provided as the extra parameter inside the method definition.
"""
a = Details()
b = Details()

a.name="radhe"
b.name="ram"

a.info()
b.info()

""" self means ae object jena par method call thay chhe """