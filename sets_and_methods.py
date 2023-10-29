"""
PYTHON SETS
        > Sets are unordered collection of data itmes.
        > store multiple items in one variable
        > enclose in {}
        > unchangable, meaning you cannot change item of the set once created.
        > do not contain duplicate items
"""

info = {"prince", 1,2,3}
print(info)

prince = {} # type <class 'dict'>
ram = set() # type <class 'set'>
print(type(prince))
print(type(ram))


for i in info:
    print(i)
    
    
"""
METHODS SETS
"""
s1 = {1,2,5,6}
s2 = {3,6,7}

# union(): merge the sets
s3 = s1.union(s2)
print(s3)

# update(): update sets with union of itself or other
s1.update(s2)
print(s1)

# symmetric_difference(): return those values which is not common in both sets
s11 = {"prince", "Dipesh", "Mitesh"}
s12 = {"Dipesh","Panda","Happy"}
s13 = s11.symmetric_difference(s12)
print(s13)

# difference(): s11 - s12
s14= s11.difference(s12)
print(s14)

# isdisjoint(): checks if items of given set are present in another set / no common element
print(s1.isdisjoint(s2))

# issuperset(): checks s2's element is present in s1 or not
s111 = {1,2,3,4}
s222 = {3,4}
print(s111.issuperset(s222))
print(s222.issuperset(s111))

# issubset(): check s2 is in s1 or not
print(s111.issubset(s222))
print(s222.issubset(s111))

# remove(), discard() :  to remove items from set
# if element is not present in set remove show error, discard can not show any error

# pop(): remove the last item of the set but the catch is that we dont know which item gets popped as sets are unordered.
name = {"dipesh", 'prince', 'mitesh'}
namePopped = name.pop()
print(name)
print(namePopped)

# del: it is a keyword that delete entire set
del name
# print(name)

# cleare(): remove all items and print empty set
s111.clear()
print(s111)