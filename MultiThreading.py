""" 
MULTITHREADING IN PYTHON:
    > Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. 
    > In Python, we can use the threading module to implement multithreading.
"""
import threading

""" 
CREATING A THREAD
    > To create a thread, we need to create a Thread object and then call its start() method. 
    > The start() method runs the thread and then to stop the execution, we use the join() method.
    
FUNCTIONS:
    (1) threading.Thread(target, args): 
        > This function creates a new thread that runs the target function with the specified arguments.
    (2) threading.Lock(): 
        > This function creates a lock that can be used to synchronize access to shared resources between threads.
"""
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping for {seconds} sec.")
    time.sleep(seconds)
    return seconds
    

def main():
    time1 = time.perf_counter()

    # normal code
    # func(4)
    # func(2)
    # func(1)

    # same code using thread
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    # calculating time
    time2 = time.perf_counter()
    print(time2 - time1)

def poolingDemo():
    with ThreadPoolExecutor() as executer:
        # future1 = executer.submit(func, 5)
        # future2 = executer.submit(func, 2)
        # future3 = executer.submit(func, 3)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        
        l=[3,5,6,8]
        results = executer.map(func,l)
        for r in results:
            print(r)

poolingDemo()

