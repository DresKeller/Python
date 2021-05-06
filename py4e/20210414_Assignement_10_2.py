fname = 'mbox-short.txt'

fh = open(fname)
counts = {}

for line in fh:

    words = line.split()
#    print(words)


    if len(words)<1  or words[0] != ('From') :
        continue

#    print(words[0])
    h = words[5].split(':')[0]

#    print(h)
    counts[h] = counts.get(h, 0) + 1

l = len((sorted(counts.items())))

for i in range(l)  :
   print(sorted(counts.items())[i][0],sorted(counts.items())[i][1])

# print("There were", count, "lines in the file with From as the first word")
