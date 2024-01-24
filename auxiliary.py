from urllib.error import HTTPError
import requests


r = requests.get('https://api.github.com')

if r.status_code == 200:
    print("GitHub API Successful")

elif r.status_code == 404:
    print("GitHub API Not OK")


url = 'https://api.github.coml'
try:
    response = requests.get(url)

    response.raise_for_status()
except HTTPError as err:
    print(f'HTTP Error : {err}')
except Exception as err:
    print(f'Unexpected Error : {err}')
