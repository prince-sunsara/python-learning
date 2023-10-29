"""
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
# now append three random characters at the starting and the end 
# i.e ring = mnbingrkjh
# else:
#   simply reverse the string 
# i.e of = fo

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
"""

inputString = input("Enter the string: ")
print(f"Your string is {inputString}")

words = inputString.split(" ")

# coding = True
coding = False
if(coding):  
    newString = []
    for word in words:
        if len(word) >=3:
            r1 = "rav"
            r2 = "van"
            newWord = r1 + word[1:] + word[0] + r2
            newString.append(newWord)
        else:
            newString.append(word[::-1])
    print(" ".join(newString))
else:
    newString = []
    for word in words:
        if len(word) >=3:  
            newWord =  word[3:-3] 
            newWord = newWord[-1] + newWord[:-1] 
            newString.append(newWord)
        else:
            newString.append(word[::-1])
    print(" ".join(newString))