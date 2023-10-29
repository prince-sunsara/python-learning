"""
# ACCESS SPECIFIERS / MODIFIERS :
    > access specifier or modifier in python programming are used to  limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.
    
    TYPES
    
        > Public access modifier
        > Private access modifier
        > Protected access modifier
"""

""" 
PUBLIC ACCESS SPECIFIER IN PYTHON:
    > all the variables and methods (member functions) in python are by default public.
    > Any instance variable in class followed by the 'self' keyword ie. self.var_name are public accessed.
"""
# class Student:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
# p = Student(21, "prince")
# print(p.age)
# print(p.name)

""" 
PRIVATE ACCESS MODIFIER:
    > private members of a class are those members which are only accessible inside the class.
    > We cannot use private members outside of class.
    
    > In python, there is no strict concept of "private" access modifier like in some other programming languages.
    > However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore(__).
    > this is known as a 'weak internal use indicator' and it is a convention only, not a strict rule.
    > code outside the class can still access these 'private' variables and methods, but it is generally understood that they should not be accessed or modified.
"""
# class Student:
#     def __init__(self, age, value):
#         self.__age = age # An indication or private variable
#         def __fullName(self):
#             self.y = 34
#             print(self.y)

# class Subject(Student):
#     pass

# obj = Student(21, "Prince")
# obj1 = Subject

# # calling by object of class student
# print(obj.__age)
# print(obj.__fullName())

# # calling by object  of class Subject
# print(obj1.__age)
# print(obj1.__funName())

# " You cannot access private variable directly but you can access it indirectly "
# print(obj._Student__age)

""" 
NAME MANGLING:
    > Name mangling in python is a technique used to protect class-private and superclass-private attribute from being accidenally overwritten by subclasses.
    > Name of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.
"""
# class MyClass:
#     def __init__(self):
#         self._nonmangled_attribute = "I am a nonmangled attribute"
#         self.__mangled_attribute = "I am a mangled attribute"

# my_object = MyClass()

# print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute) # Throws an AttributeError
# print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute

""" 
PROTECTED ACCESS MODIFIER:
    > In OOP, the term "protected" is used to describe a member (i.e. a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses.
    > in python, the convention for indicating that a member is protected is to prefix its name with a single underscore(_), for i.e. a class method called _my_method, it is indicating that the method should  only be accessed by the class itself and its subclasses.
    > It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member.
    > The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.
"""
class Student:
    def __init__(self):
        self._name = "prince"
    def _funName(self):    # protected method
        return "Prince Sunsara"
    
class Subject(Student): # inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())