""" 
THE TIME MODULE IN PYTHON:
    > The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions.
    > This module is part of the Python Standard Library 
"""
import time
"""
time.time()
    > returns current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized).
    > The returned value is based on the computer's system clock and is affected by time adjustments made by the operating system, such as daylight saving time.
"""
print(time.time())

""" 
time.sleep()
    > The time.sleep() function suspends the execution of the current thread for a specified number of seconds.
    > This function can be used to pause the program for a certain period of time, allowing other parts of the program to run, or to synchronize the execution of multiple threads.
"""
print("I am prince")
time.sleep(3)
print("it is printed after 3s")

""" 
time.strftime()
    > The time.strftime() function formats a time value as a string, based on a specified format. 
    > This function is particularly useful for formatting dates and times in a human-readable format, such as for display in a GUI, a log file, or a report.
"""
t = time.localtime()
ft = time.strftime("%H:%M:%S %Y-%m-%d", t)
print(ft)