# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingW9RQ5H-YE4/
def solution(A, K):
    # write your code in Python 3.6

    if A == []:
        return A

    N = len(A)
    K = K % N
    
    return A[N - K:] + A[:N - K]
