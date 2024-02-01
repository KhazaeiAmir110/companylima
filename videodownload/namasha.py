import requests
import re
from bs4 import BeautifulSoup


dict_quality = {
    '1080' : 0,
    '720' : 1,
    '480' : 2,
    '360' : 3,
    '240' : 4,
    '144'  :5
}

class Scraper:
    def __init__(self, url , quality):
        self.url = url
        self.quality = quality


    def get_all_link(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        vide_link = soup.find_all('a', href=re.compile('.mp4'))
        links = [link['href'] for link in vide_link]
        return links

    def get_qualities(self):
        links = self.get_all_link()
        qualities = list(dict_quality.keys())
        available_quality = []
        for quality in range(len(links)):
            available_quality.append(qualities[quality])

        return available_quality


    def get_link(self):
        links = self.get_all_link()
        available_qualities = self.get_qualities()

        if self.quality not in available_qualities:
            raise KeyError(self.quality)

        else:
            link = links[dict_quality[self.quality]]
            return link


class Main:
    def __init__(self, url, quality):
        self.url = url
        self.quality = quality
        self.scraper = Scraper(url, quality)


    def download(self):
        video_url = self.scraper.get_link()

        with open('film.mp4', 'wb') as file:
            print('Downloading...', end='')
            response = requests.get(video_url, stream=True)
            total = response.headers.get('content-length')
            if total is None:
                return "Error downloading video."
            else:
                down = 0
                total = int(total)
                for data in response.iter_content(chunk_size=4096):
                    file.write(data)
                    down += len(data)
                    done = int(50 * down / total)
                    print('\r[{}/{}]'.format('=' * done, ' ' * (50-done)), end='')

s = Main('https://www.namasha.com/v/Ntteiyrb', '720')
s.download()
