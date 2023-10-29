"""
PYTHON TUPLES 
    > Tuples are ordered collection of data items
    > enclosed withing ()
    > unchangable / immutable
"""

tup = (1,2,3, "prince")

""" 
METHODS TO MANIPULATE TUPLES
    > if you want to manipulate tuple then you have to convert it into list
"""
countries = ("India", "America", "Pakistan","china","Russia")
temp = list(countries)
temp.append("Japan")
temp.pop(2)
countries = tuple(temp)
print(countries)


# count(element) returns number of times the given element appears in the tuple
# index(element, start, end) return first occurence of the given element from the tuple
