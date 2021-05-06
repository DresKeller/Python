
# fname = input("Enter file name: ")
# fh = open(fname)

fh = open('romeo.txt')

lst = list()
for line in fh:
    h1 = line.split()
    h2 = len(h1)
    for i in range(h2):
        if h1[i] not in lst:
            lst.append(h1[i])

lst.sort()
print(lst)
