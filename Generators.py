""" 
GENERATORS IN PYTHON
    > it is special type of functions that allows you to create an iterable sequence of values.
    >  A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it.
    >  Generators are a powerful tool for working with large or complex data sets, as they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.
    
CREATING A GENERATOR:
    > create generator using the yeild statement in a function
    > the yield statement returns a value from the generator and suspends the execution of the function until the next value is requested.
"""
def my_gen():
    for i in range(5):
        yield i
gen = my_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j)
    

""" 
BENEFITS OF GENERATORS: 
    > They allows you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory. This makes generators a powerful tool for working with large or complex data sets, as you can generate tha values as you need them, rather than having to store them all in memory at once.
    > They are laze, which means that the values are generated when they are required. This allows you to generate the values in a more efficient and memory-friendly manner, as you don't have to generate all the values up front.
"""