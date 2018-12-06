# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingQWQGEW-G5X/
def solution(A):
    # write your code in Python 3.6
    A = sorted(A)

    for i in range(len(A)):
        if i + 1 != A[i]:
            return 0

    return 1
