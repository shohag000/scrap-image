import re
import requests, urllib
from bs4 import BeautifulSoup

site = 'https://unsplash.com/t/wallpapers'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]

x=0
image = None
for url in urls:
    if url[:1]=="/":
        pass
    else:
        image = url
        print(image)
    x= x+1
    output = open("images/{}.jpg".format(x),"wb")
    output.write(urllib.request.urlopen(image).read())
    output.close()
