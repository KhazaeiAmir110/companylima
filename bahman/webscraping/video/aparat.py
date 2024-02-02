import requests
import re
import random
from bs4 import BeautifulSoup


"""
Aparat, because it is written with JavaScript, its videos cannot be downloaded.
"""
def download(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=re.compile('480p\.mp4'))

    for link in links:
        linkl = link.get('href')
        name = random.randrange(1,1000)
        with requests.get(linkl, stream=True) as r:
            with open(str(name) + '.mp4', 'wb') as file:
                for video in r.iter_content(chunk_size=1024):
                    file.write(video)


# download('https://www.aparat.com/v/Ev3mp')

def aparat(url, quality=None):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    body = soup.find('body')
    xq = body.find('div', class_='episode_container')
    div = body.find_all('div', attrs={'class': 'app'})
    li = div[0].find_all('li')
    for di in li:
        print(di)

    print(body)

aparat('https://www.aparat.com/v/Ev3mp')