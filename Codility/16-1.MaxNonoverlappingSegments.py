# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingUUTBR2-6XZ/
def solution(A, B):
    # write your code in Python 3.6
    N = len(A)
    
    if N == 0:
        return 0
    
    i, j, result = 1, 0, 1
    while i < N and j < N:
        if A[i] > B[j]:
            j = i
            i += 1
            result += 1
        else:
            i += 1
    
    return result
