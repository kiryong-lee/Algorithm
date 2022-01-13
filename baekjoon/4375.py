
while True:
    try:
        n = int(input())
        target = 1
        while True:
            if target % n == 0:
                break
            target = target * 10 + 1

        print(len(str(target)))
    except EOFError:
        break
