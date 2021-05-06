fname = 'mbox-short.txt'

fh = open(fname)
counts = {}

for line in fh:
    if not line.startswith('From:') :
        continue
    adr = line.split()[1]
    counts[adr] = counts.get(adr, 0) + 1

maxanz = 0
maxadr = 0

for adr, anz in counts.items():
    if maxanz is None or anz > maxanz:
        maxadr = adr
        maxanz = anz


print(maxadr, maxanz)
