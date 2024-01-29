import requests
import re
import random
from bs4 import BeautifulSoup

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


download('https://www.aparat.com/v/Ev3mp')