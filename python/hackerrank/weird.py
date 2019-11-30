def weird(num):
    if num % 2 == 0 and num > 20:
        print('Not Weird')
    elif num % 2 == 0 and num > 5:
        print('Weird')
    elif num % 2 == 0 and num <= 5:
        print('Not Weird')
    else:
        print('Weird')

weird(22)
weird(16)
weird(4)
weird(33)
