# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingTZEPJU-P6A/
def solution(A, K):
    # write your code in Python 3.6

    if A == []:
        return A

    A_size = len(A)
    K = K % A_size

    for i in range(K):
        last = A.pop()
        A.insert(0, last)

    return A
