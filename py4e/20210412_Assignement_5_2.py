largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    try:
        if largest is None:
            largest = int(num)
            smallest = int(num)
        else:
            if int(num) > largest:
                largest = int(num)
            if int(num) < smallest:
                smallest = int(num)

    except:
        if num == 'done':
            break
        else:
        	print('Invalid input')

print("Maximum is", largest)
print("Minimum is", smallest)
