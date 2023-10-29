""" 
HOW IMPORTING IN PYTHON WORKS
    > Importing in Python is the process of loading code from a Python module into the current script. 
    > This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.
    > Once a module is imported, you can use any of the functions and variables defined in the module by using the dot notation
"""

# # how to import
# import math

# # how to use
# result = math.sqrt(9)
# print(result)

""" 
FROM KEYWORD
    > You can also import specific functions or variables from a module using the from keyword.
"""
# from math import pi
# print(pi) 

""" 
IMPORT EVERYTHING
    > It's also possible to import all functions and variables from a module using the * wildcard. 
    > However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from.
"""
# from math import *

# result = sqrt(9)
# print(result)  

# print(pi)  

""" 
THE 'AS' KEYWORD
"""
# import math as m

# result = m.sqrt(9)
# print(result) 

# print(m.pi)  

"""
THE DIR FUNCTION
"""
# import math
# print(dir(math))

''' 
IMPORT EXTERNAL FILE
'''
from functions import add, average
add(99,1)
average(50, 30)