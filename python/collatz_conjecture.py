def collatz(num):
    arr = [num]
    while num > 1:
        if num % 2 == 0:
            num //= 2
            arr.append(num)
        else:
            num = (num * 3) + 1
            arr.append(num)
    print(arr)


collatz(4)
collatz(10)
collatz(20)
collatz(33)
collatz(55)
collatz(155)
