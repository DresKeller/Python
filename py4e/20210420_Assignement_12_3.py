# Assignment: Following Links in HTML Using BeautifulSoup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#url = input('Enter Url: ')
#count = int(input("Enter count: "))
#position = int(input("Enter position:"))

url = 'http://py4e-data.dr-chuck.net/known_by_Marybeth.html'
count = 7
pos = 18

print('Enter Count:', count)
print('Enter Position:', pos)
print('Retrieving:', url)

for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')

    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)

    print('Retrieving:', s[pos-1])
#    print(t[pos-1])
    url = s[pos-1]

print('Name:', t[pos-1])
