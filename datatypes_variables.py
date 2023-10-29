"""
    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType    
"""

a = 123 #number
b = "prince" #string
c = True #bool
d = None #none
print("type of a is: ",type(a))
print("type of b is: ",type(b))
print("type of c is: ",type(c))
print("type of d is: ",type(d))

# list collection of different or same datatypes
# lists are mutable
list1 = [1,2.5,"prince",[3,4]]
print(list1)

# tupple same as tuple
# immutable
tuple_one=(90,'abc',True,[67])
print(tuple_one)

# dict: dictionary, key-value pair, mapped data
dict={'name':'prince','age':8}
print(dict)