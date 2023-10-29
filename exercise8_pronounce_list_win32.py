""" 
EXERCISE 8:
    > Write a program to pronounce list of names using win32 API. If you are given a list l as follows:
    l = ["Rahul", "Nishant", "Harry"]
    
    Your program should pronouce:
    
        Shoutout to Rahul
        Shoutout to Nishant
        Shoutout to Harry
"""
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

names = ["Sweety", "prince", "bindiya", "kashish"]

for name in names:
    speak.Speak(f"Good morning {name}. how are you?")