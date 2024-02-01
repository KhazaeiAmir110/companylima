import requests
from bs4 import BeautifulSoup

url = 'https://www.mongard.ir/articles/51/python-advanced-courses/'

response = requests.get(url)

content = BeautifulSoup(response.content, 'html.parser')

epi_list = []

epi_table = content.find_all('table', class_='table-bordered')

for table in epi_table:
    headers = []
    headers.append(table.find('tr').text)
    print(headers)
