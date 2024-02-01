import requests
from bs4 import BeautifulSoup


url = 'https://www.mongard.ir/courses/python-web-scraping/'

page = requests.get(url)

content = BeautifulSoup(page.text, features="html.parser")

# all code
# print(content)

# find
print(content.find('h1'))

print('text : ' + content.find('h1').text)

print(content.find('h2'))
# filter find
print(content.find('h2').attrs)


# find all
print(content.find_all('h2'))

# select
print(content.select('title'))

print(content.select('p > a'))