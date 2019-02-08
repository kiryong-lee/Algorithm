# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training9D49RE-YD6/
def solution(A):
    # write your code in Python 3.6
    
    N = len(A)
    for i in range(N):
        if A[i] < 0:
            A[i] = -A[i]
        else:
            break
    
    A = sorted(A)
    result = 0
    before = -1
    for number in A:
        if before != number:
            before = number
            result += 1
    
    return result
