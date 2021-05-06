largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    try:
        if num is None:
            largest = float(num)
            smallest = float(num)
        else:
            if float(num) > largest:
                largest = float(num)
            if float(num) < smallest:
                smallest = float(num)

    except:
        if num = 'done':
            break
        print('Invalid input')

print("Maximum is", largest)
print("Minimum is", smallest)
