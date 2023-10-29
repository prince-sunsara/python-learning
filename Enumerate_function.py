"""
ENUMERATE FUNCTION IN PYTHON
    > built-in function that allows you to loop over a sequence(list, string, tuple)
    > and get the index and value of each element in the sequence at the same time.
"""

result = ['prince', 'radhe', 'dipesh', 'mitesh']

'''
for v in enumerate(result):
    print(v)
    # output
    # (0, 'prince')
    # (1, 'radhe')
    # (2, 'dipesh')
    # (3, 'mitesh')
'''
 
for index, marks in enumerate(result): # you have to right index first
    print(index, marks) 