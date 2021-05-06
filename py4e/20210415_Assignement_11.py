import re

fname = 'regex_sum_1197743.txt'

fh = open(fname)
s = 0

for line in fh:
    h1 = re.findall('[0-9]+', line)
    if len(h1) > 0 :
        h2 = len(h1)
        for i in range(h2) :
            s = s + int(h1[i])

print(s)
