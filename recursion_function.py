""" 
RECURSION FUNCTION IN PYTHON :
    > function called in same function
    > Recursion is the process of defining something terms or itself.
"""
# fectorials of n
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
   
print(fact(5))


# fibbonacci series
def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb(n-2)+fibb(n-1)
    

for n in range(0, 10):
    print(fibb(n))