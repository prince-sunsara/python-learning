""" 
FUNCTION CACHING IN PYTHON: 
    > Function caching is a technique for improving the performance of a program by storing the result of a function call so that you can reuse the result instead of recomputing them every time the function is called.
    > this can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently.
    > in pythong, function caching can be achived using the 'functools.lru_cache' decorator which is used to cache the result of function so that you can reuse the result instead of recomputing them every time the function is called.
"""

# import functools

# @functools.lru_cache(maxsize=None)
# def fibb(n):
#     if n < 2:
#         return n
#     return fibb(n-1) + fibb(n-2)

# print(fibb(20))

""" 
BENEFITS OF FUNCTION CACHING:
    > By caching the results of a function, you can avoid having to recompute the results every time the function is called, which can save a significant amount of time and computational resources.
    > it can simplify the code of a program by removing the need to manually cache the results of a function. With the functools.lru_cache decorator, the caching is handled automatically, so you can focus on writing the core logic of your program.
"""

# another ex
import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(10))
print("done for 10")
print(fx(20))
print("done for 20")
print(fx(30))
print("done for 30")

print(fx(10))
print("done for 10")
print(fx(20))
print("done for 20")
print(fx(40))
print("done for 40")
