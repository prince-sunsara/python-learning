""" 
SUPER KEYWORD:
    > The super() keyword in python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent clasees.
    > when a class inherits from a parent class, it override or extend the methods defined in the parent class.
    > however sometimes you might want to use the parent class method in the child class. this is where super() keyword comes in handy.
    
    > A super object is an instance of a class that inherits from another class. It has all the attributes and methods of its parent class.
"""
# class ParentClass:
#     def parent_method(self):
#         print("I am parent class method")

# class ChildClass(ParentClass):
#     def child_method(self):
#         print("I am child class method")
#         super().parent_method()
# c = ChildClass()
# c.child_method()

""" 
In below example, the ChildClass inherits from both ParentClass1 and ParentClass2. The child_method calls the parent_method of the first parent class using the super() keyword.
"""

class ParentClass1:
    def parent_method(self):
        print("This is the parent method of ParentClass1.")

class ParentClass2:
    def parent_method(self):
        print("This is the parent method of ParentClass2.")

class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()