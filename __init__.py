from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('video')
fhand = open('links.txt', 'wb')
for tag in tags:
    src = tag.get('src', None)
    if src is not None:
        fhand.write(src.encode() + "\n".encode())
fhand.close()