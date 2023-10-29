"""
string is immutable, 
every modified string is new object
"""

name = 'prince'
surname = "sunsara"
# multiline string
address = """ Indiranagar,
Manund, Patan,
Patan, Gujarat, 384260
"""

# index
print(name[1])

# looping
for i in name:
    print(i)

# length 
print(len(name))
    
# slicing = [startIndex:endIndex]
print(name[:4])
print(name[2:4])
print(name[2:])
print(name[:-3]) # [:len(name)-3]
print(name[-3:-1]) 


# other methods 
print(name.upper())
print(name.lower())

# rstrip(): removes tailing charasters
print("!!!!!!prince!!!!!!!!!".rstrip('!'))

# replace
print(name.replace('prince', 'Princess'))

a = "my name is prince"

# split 
print(a.split(' '))

# capitalize()
print(a.capitalize())

# count
print (a.count('n'))

# endwith
print(a.endswith(('is')))

# find: give first occurence of any word, give -1 if condition error
print(a.find('n'))

# index: give first occurence of any word
print(a.index('is'))

b = "MyNameIsPrince"
# isalnum: A-Z, a-z, 0-9
print (a.isalnum())
print (b.isalnum())

# isLower

# isprintable()
print(a.isprintable())

# isspace()
print(a.isspace())

c = "My Name Is Prince"
# istitle()
print(a.istitle())
print(c.istitle())

# swapcase() : upper to lower and vice-cersa
print(a.title())