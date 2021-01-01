import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


quotes = soup.find_all('span','text')
authors = soup.find_all('small', 'author')
tags = soup.find_all('div','tags')

for i in range(0,len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a','tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)

