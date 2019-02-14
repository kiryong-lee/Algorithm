# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingFTMV89-JX7/
def solution(A):
    # write your code in Python 3.6

    B = sorted(A)

    diff = -1
    for i in range(1, len(B), 2):
        if B[i - 1] != B[i]:
            diff = B[i - 1]
            break

    if diff == -1:
        diff = B.pop()

    return diff
