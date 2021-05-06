import os
os.listdir("/")

fhand = open('mbox-short.txt')

count = 0
sconf = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence') :
        count = count + 1
        startpos = line.find('0.')
        sconf = sconf + float(line[startpos:startpos+6])

print(count)
print(sconf)
print('Average spam confidence:', sconf/count)
