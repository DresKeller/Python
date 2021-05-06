text = "X-DSPAM-Confidence:    0.8475";

startpos = text.find('.')-1

print(float(text[startpos:startpos+6]))
