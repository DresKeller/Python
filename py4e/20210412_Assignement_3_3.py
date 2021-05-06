score = input("Enter Score: ")
try:
	score = float(score)

except:
    print('not a numeric score!')
    exit()

if score < 0:
    print('outside range! (too small)')
    quit()

if score > 1:
    print('outside range! (too big)')
    quit()

if score >= 0.9:
    print('A')

elif score >= 0.8:
    print('B')

elif score >= 0.7:
    print('C')

elif score >= 0.6:
    print('D')

else:
    print('F')
