import urllib.error, urllib.request, urllib.parse
import json

target = 'http://py4e-data.dr-chuck.net/json?'
#    address = input('Enter location: ')
#    address = 'South Federal University'
address = 'University of Akron'

url = target + urllib.parse.urlencode({'address': address, 'key' : 42})
print('Retriving', url)

data = urllib.request.urlopen(url).read()
print('Retrived', len(data), 'characters')

Inhalt = json.loads(data)
# print(json.dumps(Inhalt, indent = 4))
print('Place id', Inhalt['results'][0]['place_id'])
