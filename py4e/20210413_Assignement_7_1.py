import os
os.listdir("/")

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

text = fh.read()
text2 = text.upper()

print(text2)




# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname,'r')

for line in fh:
    line2 = line.rstrip()
    line2 = line2.upper()
    print(line2)
