""" 
Python Lists:
    > i.g. l =[3,4,5]
    > ordered collections of data item
    > store multiple item in single variable
    > under []
    > changeable
    > range of list: listName[start:end:jumpIndex]
    > List comprehension: used to create lists from other iterables 
"""
list1 = [1,2,3,"prince"]
print(list1)

marks = [1,2,3,4,5,6,7,8,9,0]
print(marks[::2])

# list comprehension
lst = [i for i in range(10)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)

""" 
List methods
"""
l = [42, 23,1,2,3,4,5]
print(l)

# sort() sort the element
# l.sort(reverse=True)


# append(element) append the element at last

# reverse() reverse the list

# index(element) gives the index

# copy() copy original list in another variable
m = l.copy()
m[0] = 0
print(l)
print(m)

# insert(index, value) insert element at given index
# extend() add an entire list, tuple, set, dictionry to existing one

# concatenating:  list1 + list2