""" 
CUSTOM ERROR IN PYTHON
    > we can raise custom error using custom keyword.
"""

a = int(input("Enter value between 5 to 10:"))

if a<5 or a>10:
    raise ValueError('Value is not in range')


""" DEFINING CUSTOM EXCEPTIONS """