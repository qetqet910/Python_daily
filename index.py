while True:
    num = list(input())
    if(num == 0):
        break
    else:
        middle = len(num) / 2
        first = num[:middle]
        last = num[middle:]
        print()
        # if(len(num) % 2 != 0 and ):