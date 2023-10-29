""" 
EXERCISE 10: DRINK WATER REMINDER
    > Write a python program which reminds you of drinking water every hour or two.
    > Your program can either beep or send desktop notifications for a specific operating system
"""
import time
from plyer import notification
import win32com.client as wincom
 
speak = wincom.Dispatch("SAPI.SpVoice")

if __name__=="__main__":
        notification.notify(
            title = "Reminder",
            message="Hey Prince, Drink some water!",
            timeout=2
)   
        speak.Speak("Hey Prince, Drink some water!")
        # waiting time
        time.sleep(5)

