""" 
REQUESTS MODULE IN PYTHON
    > python requests module is an HTTP library that enables developers to send HTTP requests in python.
    > it enables you to send HTTP requests using python code and makes it possible to interact with APIs and web services.
    > to install
        pip install requests
"""
import requests

# # GET REQUEST
# response = requests.get("https://www.google.com")
# print(response.text)


# # POST REQUEST
# url = "https://jsonplaceholder.typicode.com/posts"
# data = {"title": "prince", "body": "buddy", "userId": 7}
# headers = {'Content-Type': 'application/json'}
# response = requests.post(url, headers=headers, json=data)
# print(response.text)


""" 
bs4 Module
    > it called BeautifulShoup which is used for web scraping in python.
"""

from bs4 import BeautifulSoup
r = requests.get("https://www.geeksforgeeks.org/python-beautifulsoup-find-all-class/")

soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

for heading in soup.find_all("h2"):
    print(heading.text)