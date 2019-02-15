# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingUZV5UZ-5DR/
def solution(A):
    # write your code in Python 3.6
    A.sort()
    
    N = len(A)
    if A[0] >= 0:
        return A[0] + A[0]
    elif A[N - 1] <= 0:
        return abs(A[N - 1] + A[N - 1])
    
    minimal_abs = 2000000000
    p, q = 0, N - 1
    while A[p] <= 0 and A[q] >= 0:
        sum_abs = abs(A[p] + A[q])
        if sum_abs < minimal_abs:
            minimal_abs = sum_abs
        
        if abs(A[p]) > abs(A[q]):
            p += 1
        elif abs(A[p]) < abs(A[q]):
            q -= 1
        else:
            return 0
    
    return minimal_abs
