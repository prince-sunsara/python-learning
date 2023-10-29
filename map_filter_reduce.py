""" 
MAP, FILTER AND REDUCE
    >  map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. 
    > These functions are known as higher-order functions, as they take other functions as arguments.
"""

"mere hissse me tu nahi he"

""" 
MAP:
    > the map function applies a function to each element in sequence and returns a new sequence containing the transfrormed elements.

    map(function, iterable)
    
    > function argument is a function that is applied to each element in the iterable. 
    > The iterable argument can be a list, tuple, or any other iterable object.
"""
# numbers =[1,2,3,4,5]

# maped_fun = map(lambda x: x*x, numbers)
# print(list(maped_fun))

"""
FILTER:
    > filters a sequence of elements based on a given predicate (function that returns boolean value) and return a new sequence containing only the elements that meet the predicate.
    
    filter(predicate, iterable)
    
    > the predicate argument is a function that returns a boolean value and is applied to each element in tha iterable argument
    > iterable argument can be a list, tuple or any other iterable objects.
"""

# evens = filter(lambda x: x%2 == 0, numbers)
# print(list(evens))

""" 
REDUCE:
    > is a higher order function that applies a function to a sequence and returns a single value.
    > it is a part of functools modules in python
    
    reduce(function, iterable)

    > the function argumebt is a function that takes in two args and returns a single value.
    > the iterable args is a sequence of element, such as a list tuple.
    
    > the reduce func applies the function to the first two elements in the iterable and then applies the func result and the next element, and so on. the reduce functions returns the final result.
"""

from functions import reduce

numbers =[1,2,3,4,5]

sum = reduce(lambda x,y: x+y, numbers)
print(sum)