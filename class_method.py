""" 
CLASS METHOD:
    > classes are way to define custom data types that can store data and define functions that can manipulate that data.
    > A class method is a type of method that is bound to tha class and not theinstance of tha class. in other words, it opeates on ha class as a whole, rather than on a specific instance of tha class.
    > They are defined using the '@classmethod' decorator, followed by a function definition.
    > first argument of the function is always 'cls', which represents the class itself.
"""  
class ClassMethod:
    company = "apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    @classmethod
    def changeCompany(cls, newName):
        cls.company = newName
        
a = ClassMethod()
a.name = "prince"
a.show()
print(ClassMethod.company)
a.changeCompany("Banana")
a.show()
print(ClassMethod.company)

''' 
    > class method e class ne represent kre and class ni andr kai change krvu hoy globaly to e classmethod ni mdd thi thay
'''