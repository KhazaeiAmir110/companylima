import requests
import re
from bs4 import BeautifulSoup


def get_all_link(url, quality):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    vide_link = soup.find_all('a', href=re.compile(f'{quality}p.mp4'))
    links = [link['href'] for link in vide_link]
    return links[0]

link = get_all_link('https://www.namasha.com/v/yqp7QWIF', 360)

with open('simple.mp4', 'wb') as f:
    response = requests.get(link, stream=True)
    for data in response.iter_content(1024):
        print("Downloading...", data.decode('utf-8'))
        f.write(data)
    print("Download Success!!!!")