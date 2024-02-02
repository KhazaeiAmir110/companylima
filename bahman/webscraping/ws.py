from bs4 import BeautifulSoup
import requests

url = "https://www.skysports.com/premier-league-table"
response = requests.get(url)
r = response.text

# with open('index.html', 'a') as f:
#     f.write(r)
#     print('success')
# ----------------------------------

soup = BeautifulSoup(response.text, 'html.parser')


table = soup.find('table')

# print(type(table)) => class
tr = table.find_all('tr')
# write to file
# with open('tr.html', 'a') as f:
#     f.write(r)

# for row in tr:
#     print(row.text)
#     for td in row:
#         print(td.text)

"""
            select_one 
            
class : ----------->>>>>> 'tag.classname' 
id : ------------->>>>>>> 'tag#idangme'
"""
data_1_1 = soup.select_one('.standing-table__table')

data_1_2 = soup.select_one('table', {'class': 'standing-table__table'})

# print(data_1_1 == data_1_2) => True

# print(data_1)

data_2 = soup.select_one('td.standing-table__cell')
print(data_2)


