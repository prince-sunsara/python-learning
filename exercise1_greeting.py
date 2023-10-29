import time
import os

os.system('python --version')

# print(time.gmtime())
get_time = time.strftime("%A, %B %d, %Y, %H:%M:%S")
print(get_time)

hour = int(time.strftime("%H"))
print(hour)

if(hour<12):
    print("Good Morning!!")
elif(hour<16):
    print("Good Afternoon!!")
elif(hour<20):
    print("Good Evening!!")
else:
    print("Good Night!!")
    