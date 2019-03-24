# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training43S6DZ-QCR/
def solution(A):
    # write your code in Python 3.6
    A.sort()

    a = A[-1] * A[-2] * A[-3]
    b = A[0] * A[1] * A[-1]
    
    if a > b:
        return a
    else:
        return b
