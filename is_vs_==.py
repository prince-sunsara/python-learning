''' 
'is' vs '==' in Python
    >  is and == are both comparison operators that can be used to check if two values are equal.
    > The is operator compares the identity of two objects
    > while the == operator compares the values of the objects.
    >  is will only return True if the objects being compared are the exact same object in memory
    > while == will return True if the objects have the same value.
'''
# is -> exact location of object in memory
# == -> value

# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)  # True
# print(a is b)  # False

'''
    > in Python, strings, tuples and integers are immutable
    > which means that once they are created, their value cannot be changed. 
    > This means that, for strings and integers, is and == will always return the same result:
'''
a = "hello"
b = "hello"
c = (1,2)
d = (1,2)

print(a == b)  # True
print(a is b)  # True
print(c == d)  # True
print(c is d)  # True

# a = 5
# b = 5

# print(a == b)  # True
# print(a is b)  # True