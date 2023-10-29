""" 
READLINES()  METHOD:
    > reads a single line from the file
    > use loop to read multiple lines
    > The readlines() method reads all the lines of the file and returns them as a list of strings.
"""
# f = open("myfile.txt", 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

""" 
WRITELINE() METHOD:
    > write sequence of strings to a file
    > the sequence can be any iterable object, such as list, tuple
    >  writelines() method does not add newline characters between the strings in the sequence. 
    > If you want to add newlines between the strings, you can use a loop to write each string separately:
"""

# f = open("myfile2.txt", 'w')
# lines = ["prince\n", "Dipesh\n", "Radhe\n"]
# f.writelines(lines)

""" 
SEEK() AND TELL() FUNCTIONS:
    > These functions are used to work with file objects and their positions withing a file. 
    > These functions are part of built-in IO module, which provides a consistent interface for reading and writing to various file- like objects, such as files, pipes, and in memory buffers.
"""

""" 
seek() 
    > seek() function moves pointer at given position (in bytes).
    > the position is specified in bytes, and you can move either forward and backward from the current position.
"""
# with open("myfile2.txt", 'r') as f:
#     # Move to the 10th byte in the file
#     f.seek(10)
#     # Read the next 5 bytes
#     data = f.read(5)
    
"""
tell() 
    > tell() function tells current location within the file.
    >  This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position.
"""
# with open('myfile2.txt', 'r') as f:
#   # Read the first 10 bytes
#   data = f.read(10)

#   # Save the current position
#   current_position = f.tell()

#   # Seek to the saved position
#   f.seek(current_position)
  
""" 
truncate() function:
    > if you want to truncate the file to a specific size, you can use the truncate function.
"""
with open('myfile2.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read(10)

  # Save the current position
  current_position = f.tell()

  # Seek to the saved position
  f.seek(current_position)