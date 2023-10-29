""" 
OPERATOR OVERLOADING IN PYTHON:
    > Operator Overloading is a feature in python that allows to redefine the behaviour of the mathematical and comparison operators for custom data types.
    > This means that you can use the standard mathematical operators(+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str.
    > Operator overloading allows you to create more readable and intuitive code.
    > You can overload an operator in Python by defining special methods in your class. These methods are identified by their names, which start and end with double underscores (__). 
    > Here are some of the most commonly overloaded operators and their corresponding special methods:
    + : __add__
    - : __sub__
    * : __mul__
    / : __truediv__
    < : __lt__
    > : __gt__
    == : __eq__
    
"""
class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, x):
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
    
    def __sub__(self, x):
        return Vector(self.i - x.i, self.j - x.j, self.k - x.k)

v1 = Vector(1,2,3)
print(v1)

v2 = Vector(6,5,4)
print(v2)

print(v1+v2)
print(type(v1+v2))

print(v2-v1)
print(type(v2-v1))