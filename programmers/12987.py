
def solution(A, B):
    A.sort()
    B.sort()
    
    a, b = 0, 0
    win_count = 0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            win_count += 1
            a += 1
            b += 1
        else:
            b += 1

    return win_count
