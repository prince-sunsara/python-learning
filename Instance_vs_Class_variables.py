""" 
INSTANCE VS CLASS VARIABLES:
    > in python, variables can be defined at the class level or at the instance level.
    
CLASS VARIABLES:
    > class variables are defined at the class level and are shared among all instance of the class.
    > They are defined outside of any method and are usually used to store information that is common to all instances of the class.
    # class variable class ni andr define (class ni method bar) thay and class mo gme e use kri ske, class instane thi bi use kri skay and change bi
"""
# class MyClass:
#     class_variable = "Apple"
    
#     def __init__(self, name):
#         self.name = name

#     def showDetails(self):
#         print(f"The name of company {self.class_variable} and name is {self.name}")

# a = MyClass("Prince")
# b = MyClass("Radhe")

# print(a.class_variable)

# b.class_variable = "Banana"
# b.showDetails()

""" 
INSTANCE VARIABLES:
    > Instance variables are defined at the instance level and are unique to each instance of class.
    > they are defined inside the init method and are usually used to store informaion that is specific to each instance of the class.
    # instance variable init ni andr jetla use thay ej. darek instance mate alg alg hot chhe e.
"""
class MyClass:
    def __init__(self, name):
        self.name = name

    def showDetails(self):
        print(f"The name is {self.name}")

a = MyClass("Prince")
b = MyClass("Radhe")

a.showDetails()
b.showDetails()