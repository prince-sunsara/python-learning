""" 
EXERCISE 10: FETCH NEWS FROM NEWSAPI
    > Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application
"""
import requests
import json
# b3318bf947414be9ac53dac6ce005e35
query = input("Tell me something what you like? ")

url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey=dbe57b028aeb41e285a226a94865f7a7"

r = requests.get(url)
# print(r.text)
news = json.loads(r.text)

for article in news['articles']:
    print(article['title'])
    print(article['description'])
    print("-----------------------------------------------")