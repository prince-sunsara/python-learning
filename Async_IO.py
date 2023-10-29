""" 
ASYNCHRONOUS(ASYNC) I/O:
    > it's a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner.
    > It is achieved through the use of the asyncio module and asynchronous function
"""
import asyncio
import time
import requests

async def myFun1():
    url = "https://i.pinimg.com/originals/31/06/40/310640800235b593480c62ed608f9a36.jpg"
    res = requests.get(url)
    open("img1.jpg", "wb").write(res.content)
    print("Download completed")
    
    # await asyncio.sleep(1)
    # print("fun 1")
    return 1
    
async def myFun2():
    url = "https://pixelz.cc/wp-content/uploads/2017/11/sleeping-grey-kitten-uhd-8k-wallpaper.jpg"
    res = requests.get(url)
    open("img2.jpg", "wb").write(res.content)
    print("Download completed")
    
    # await asyncio.sleep(1)
    # print("fun 2")
    return 1
    
async def myFun3():
    url = "https://thehappypuppysite.com/wp-content/uploads/2017/12/puppy9.jpg"
    res = requests.get(url)
    open("img3.jpg", "wb").write(res.content)
    print("Download completed")
    
    # await asyncio.sleep(3)
    # print("fun 3")
    return 1

async def main():
    # task = asyncio.create_task(myFun1())
    # await myFun1()
    # await myFun2()
    # await myFun3()
    L = await asyncio.gather(myFun1(), myFun2(), myFun3())
    print(L)

asyncio.run(main())