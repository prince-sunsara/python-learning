"""
OS MODULE IN PYTHON
    > OS module in python is a built-in library that provides functions for interacting with the operating system.
    > It allows you to perform a wide veriety of tasks, such as reading and writing files, interacting with the file system, running system commands.
"""
import os

# # to create 10 folders
# if (not os.path.exists("for-OS-Module")):
#     os.mkdir("for-OS-Module")    
# for i in range(0, 10):
#     os.mkdir(f"for-OS-Module/Day{i+1}")

# # to rename all 10
# for i in range(0, 10):
#     os.rename(f"for-OS-Module/Day{i+1}", f"for-OS-Module/Tutorial{i+1}")

# # list all folders/files
# folders = os.listdir("for-OS-Module")
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"for-OS-Module/{folder}"))   
    
# # get file path
print(os.getcwd())

# # change directory
# os.chdir("/Users")