N = int(input())
A = list(map(int, input().split()))

lis = [0]
for data in A:
    b_min, b_mid = 0, 0
    b_max = len(lis) - 1
    while b_min <= b_max:
        b_mid = int((b_min + b_max) / 2)
        if lis[b_mid] < data:
            b_min = b_mid + 1
        elif lis[b_mid] == data:
            break
        else:
            b_max = b_mid - 1

    if data < lis[b_mid]:
        lis[b_mid] = data
    elif data > lis[-1]:
        lis.append(data)
    elif data != lis[b_mid]:
        lis[b_mid + 1] = data

print(len(lis) - 1)
