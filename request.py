import requests

url = 'https://www.python.org'

response = requests.get(url)

# type response
print(response)

# status code
print(response.status_code)

# value
print(response.reason)


# header response
print(response.request)

# header request
print(response.request.headers)


with open('movie.jpg', 'wb') as fs:
    fs.write(response.content)

response = requests.get(url)

with open('index.txt','w') as fs:
    fs.write(str(response.headers))



url_image = 'https://my.alfred.edu/zoom/_images/foster-lake.jpg'

response = requests.get(url_image)

print(response.status_code)