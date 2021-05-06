print('ganz am Anfang')
import os
print('vorher')
os.listdir("/")
print('nachher')
fhand = open('mbox.txt')
print('fhand 1: ', fhand)

count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('Anzahl Mails: ', count)


fhand = open('mbox.txt')

zeile = 0
for cheese in fhand:
#    print(cheese)
    zeile = zeile + 1
print('Anzzahl Zeilen: ', zeile)


fhand = open('mbox.txt')

inp = fhand.read()
# print('inp: ', inp)
print('Anzahl Zeichen: ', len(inp))
print('Erste 100 Zeichen: ', inp[:100])
print('fhand 2: ', fhand)
