# Assignment: Following Links in HTML Using BeautifulSoup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://py4e-data.dr-chuck.net/known_by_Marybeth.html'

print('Enter Url:', url)

count = 8
pos = 18

print('Enter Count:', count - 1)
print('Enter Position:', pos + 1)

urllist=list()

for i in range(count):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    print('Retrieveing:',url)
    taglist = list()
    for tag in tags:
        y = tag.get('href',None)
        taglist.append(y)

#    print(taglist[2])
    url = taglist[pos]

    urllist.append(url)

print("Last Url retrieved:",urllist[-2])
# print(urllist)
