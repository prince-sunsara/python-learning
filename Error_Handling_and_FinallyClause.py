""" 
EXCEPTION HANDLING:
    > process of responding to unwanted or unexpected events when a computer program runs.
    
EXCEPTION IN PYTHON:
    > python has many built-in exceptions that are raised when your program encounters an error(something in the program goes wrong).
    
TRY....EXCEPT
    > it used in python to handle errors and exceptions.
"""

# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is :")
# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#     print("Sorry, Invalid input!")

# except Exception as e:
    # print(e)
    
# print("End of program")

""" VALUE ERROR """
# try:
#     num = int(input("Enter num: "))
# except ValueError:
#     print("Please enter integer value")
    
""" INDEX ERROR """
a = [1,2,3]
try: 
    num = int(input("Enter num: "))
    print(a[num])
except IndexError:
    print("Index error")
    
""" 
FINALLY CLAUSE:
    > part of exception handling
    > after exception block we can include it
    > it always execute
    > it is gereally used for doing the concluding taks like closing file resourses or closing database connection or may be ending the program eecution with delightfull message.
"""
try:
    l = [1,2,3,4]
    i = int(input("Enter index:"))
    print(l[i])
except:
    print("Some error occured")
finally:
    print("I am always executed!")