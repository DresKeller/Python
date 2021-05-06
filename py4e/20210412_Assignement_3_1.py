hrs = input("Enter Hours:")
h = float(hrs)
pay = float(input('Pay per Hour: '))
if h <= 40:
    totalpay = h * pay

else:
    totalpay = 40 * pay + 1.5 * (h-40) * pay

print(totalpay)
