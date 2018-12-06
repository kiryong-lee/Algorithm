# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingRDKGXK-D7G/
def solution(A):
    # write your code in Python 3.6
    B = sorted(A)

    N = len(B)
    for i in range(N -2):
        if B[i] + B[i + 1] > B[i + 2]:
            return 1

    return 0
