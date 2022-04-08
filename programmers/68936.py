
answer = [0, 0]

def recursion(arr, px, py, n):
    if n == 1:
        answer[arr[py][px]] += 1
        return

    compress = True
    for y in range(py, py + n):
        for x in range(px, px + n):
            if  arr[y][x] == 1:
                compress = False
                break
        if not compress:
            break
    if compress:
        answer[0] += 1
        return
    
    compress = True
    for y in range(py, py + n):
        for x in range(px, px + n):
            if  arr[y][x] == 0:
                compress = False
                break
        if not compress:
            break
    if compress:
        answer[1] += 1
        return
    
    recursion(arr, px, py, n // 2)
    recursion(arr, px + n // 2, py, n // 2)
    recursion(arr, px, py + n // 2, n // 2)
    recursion(arr, px + n // 2, py + n // 2, n // 2)


def solution(arr):
    recursion(arr, 0, 0, len(arr))
    return answer
    
