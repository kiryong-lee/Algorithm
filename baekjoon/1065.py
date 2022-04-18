
n = int(input())
if n < 100:
    print(n)
else:    
    count = 99
    for i in range(100, n + 1):
        a = i // 100
        b = (i % 100) // 10
        c = i % 10
        if c - b == b - a:
            count += 1
    print(count)
