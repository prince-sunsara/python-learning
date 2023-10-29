""" 
REGULAR EXPRESSION IN PYTHON:
    > regular expression or 'regex' are a powerful tool for working with string and text data in python
    > they allows you to match and manipulate string based on patterns, making it easy to perform complex string operation with just a few line of code.

METACHARACTERS IN REGEX
    [] -> Represent a character class
    ^ -> Matches the beginning
    $ -> Matches the end of line
    . -> Matches any single character except newline
    ? -> Matches zero or one occurrence.
    * -> Matches zero or more occurrences.
    | -> means OR (matches with any of the characters separated by it.)
    + -> One or more occurrences.
    {} -> Indicate number of occurrences of a preceding RE to match
    () -> enclose a group of REs
"""
import re

""" 
SEARCHING FOR A PATTERN IN RE USING RE.SERACH()
    > re.search() method either returns None (if the pattern doesn’t match), or a re.MatchObject that contains information about the matching part of the string.
    > This method stops after the first match, so this is best suited for testing a regular expression more than extracting data.
"""
# # Define a regular expression pattern
# pattern = r"[A-Z]"
# # Match the pattern against a string
# text = "Hello, world!"
# match = re.search(pattern, text)
# if match:
#     print("Match found!")
# else:
#     print("Match not found.")

""" 
SEARCHING FOR A PATTERN IN RE USING RE.FINDALL()
    > You can also use the re.findall function to find all occurrences of the pattern in a string:
"""
# pattern = r"[a-z]+at"
# text = "The cat is in the hat."
# matches = re.findall(pattern, text)
# print(matches)

""" 
EXTRACTING INFORMATION FROM A STRING
"""
text = "The email address is prince@gmail.com which is my personal."
pattern = r"\w+@\w+\.\w+"

match = re.search(pattern, text)

if match:
    email = match.group()
    print(email)