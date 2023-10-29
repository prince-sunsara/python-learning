""" 
PYTHON DICTIONARIES
    > A dictionary is a order collection of items
    > key:value pairs. 
    > The keys are unique identifier which used to access value
    > enclosed withing curly brackets {}
    > sepereted by comma(,)
"""

details = {
    'name': 'prince',
    'age': 20
}
print(details['name'])  # give an eror if not exist
print(details.get('age'))   # give None if not exist
print(details.keys())   # give every keys
print(details.values())   # give every values
print(details.items())  # return all key-value pairs
for key, value in details.items():
    print(f"The value corresponding to the key {key} is value {value}")


""" 
METHODS OF DICTONARIES
"""

# update(): update values of the key
other_details = {
    'class': "CE7",
    'rollno':'11203'
}

details.update(other_details)
print(details)

# clear(): clear the dict
# pop(): remove the item with index
# popitem(): remove the last item
# del : key word that delete the dict