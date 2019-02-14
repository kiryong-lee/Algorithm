# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingFJ38R2-X7U/
def solution(A):
    # write your code in Python 3.6
    A.sort()
    N = len(A)
    
    if N < 2:
        return 0
    
    result = 0
    for p in range(N - 2):
        q = p + 1
        r = p + 2
        while r < N:
            if A[p] + A[q] > A[r]:
                result += r - q
                r += 1
            elif q < r - 1:
                q += 1
            else:
                q += 1
                r += 1
        
    return result
