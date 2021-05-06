import urllib.request, urllib.parse, urllib.error
import json

# url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url = 'http://py4e-data.dr-chuck.net/comments_1197748.json'

print('Retrieving', url)

uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)

sum = 0
total_number = 0

for item in info["comments"]:

    total_number = total_number + 1
    sum = sum + int(item["count"])

print('Anzahl: ', total_number)
print('Total Counts', sum)
