# Extracting Data from XML

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#input = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.xml')
input = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1197747.xml')
data = input.read()
tree = ET.fromstring(data)

Summe = 0
for comments in tree.findall('comments'):
    for comment in comments.findall('comment'):
        Summe = Summe + int(comment.find('count').text)

print('Summe der Anzahlen:', Summe)
