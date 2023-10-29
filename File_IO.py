"""
FILE IO in PYTHON
    > Python provides several ways to manipulate files.
    
Opening a File:
    > Python provides the open() function to open a file. 
    > It takes two arguments: the name of the file and the mode in which the file should be opened. 
    > The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.

MODES IN FILE:
    > read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

    > write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

    > append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

    > create (x): This mode creates a file and gives an error if the file already exists.

    > text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

    > binary (b): used to handle binary files (images, pdfs, etc).
"""
# f = open("myfile.txt", "r")

""" 
READING FROM A FILE
    > Once we have a file object, we can use various methods to read from the file.
    > The read() method reads the entire contents of the file and returns it as a string.
"""
# f = open("myfile.txt", "r")
# print(f.read())


""" 
WRITING FROM A FILE
    > To write to a file, we first need to open it in write mode.
    > We can then use the write() method to write to the file.
    > Keep in mind that writing to a file will overwrite its contents. 
    > If you want to append to a file instead of overwriting it, you can open it in append mode.
"""
# f = open("myfile.txt", 'w')
# f.write("My name is prince.")


""" 
CLOSING FROM A FILE
    > It is important to close a file after you are done with it. 
    > This releases the resources used by the file and allows other programs to access it.
    > To close a file, you can use the close() method.
"""
# f.close()

""" 
THE 'WITH' STATEMENT
    > Alternatively, you can use the with statement to automatically close the file after you are done with it.
"""
with open("myfile.txt", "r") as f:
    print(f.read())