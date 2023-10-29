""" 
MULTIPROCESSING IN PYTHON:
    > Multiprocessing is a python module that provides a simple way to run multiple processes in parallel.
    > It allows you to take advantage of multiple cores or processors on your system and can significantly improve the performance of your code.

FUNCTIONS:
    (1) multiprocessing.Process(target, args): 
        > This function creates a new process that runs the target function with the specified arguments.
    (2) multiprocessing.Pool(processes): 
        > This function creates a pool of worker processes that can be used to parallelize the execution of a function across multiple input values.
    (3) multiprocessing.Queue(): 
        > This function creates a queue that can be used to communicate data between processes.
    (4) multiprocessing.Lock(): 
        > This function creates a lock that can be used to synchronize access to shared resources between processes.
"""
import multiprocessing
import requests
from concurrent.futures import ProcessPoolExecutor

def downloadFile(url, name):
    print("Downloading started...")
    res = requests.get(url)
    open(f"files/{name}.jpg","wb").write(res.content)
    print("File downloaded.")

url = "https://picsum.photos/200/300"

def mulPros():
    pros = []
    for i in range(100):
        # normal code
        # downloadFile(url, i)
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()

def poolingDemo():
    with ProcessPoolExecutor() as executer:
        l1 = [url for i in range(10)]
        l2 = [i for i in range(10)]
        results = executer.map(downloadFile,l1, l2)
        for r in results:
            print(r)



if __name__ == '__main__':
    # mulPros()
    poolingDemo()