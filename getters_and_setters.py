""" 
GETTERS IN PYTHON:
    > Getters are methods that are used to access tha values of an object's properties.
    > They are used to return the value of a specific property, and are typically defined using the @property decoder.
"""

# class MyClass:
#     def __init__(self, value):
#         self._value = value
        
#     def show(self):
#         print(f"Value is {self._value}")
    
#     @property
#     def value(self):
#         return self._value

# a = MyClass(10)
# print(a.value) # a.value won't be changable
# a.show()


"""" 
SETTERS IN PYTHON:
    > It is imp to note that the getters do not take any parameters and we cannot set the calue through getter method.
    > For that we need setter method which can be added by decorating method with @property_name.setter
"""
class ClassName:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

obj = ClassName(10)
print(obj.value)

obj.value = 20
print(obj.value)

""" 
CONCLUSION
    > getters are a convenient way to access the values of an object's properties, while keeping the internal representation of the property hidden. This can be useful for encapsulation and data validation.
"""