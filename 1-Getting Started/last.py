largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    else :
        try :
            number = int(num)
            if smallest is None:
                smallest = number
            if largest is None:
                largest = number
            if number < smallest:
                smallest = number
            if number > largest:
                largest = number
        except :
            print('Invalid input')


print("Maximum is", largest)
print('Minimun is',smallest)
