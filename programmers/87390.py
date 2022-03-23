
def solution(n, left, right):
    left = int(left)
    right = int(right)
    arr = [0] * (right - left + 1)
    
    for i in range(n):
        if (i + 1) * n < left:
            continue
        if i * n > right:
            break
        for j in range(i):
            if left <= i * n + j <= right:
                arr[i * n + j - left] = i + 1
        
        for j in range(i, n):
            if left <= i * n + j <= right:
                arr[i * n + j - left] = j + 1
    
    return arr
