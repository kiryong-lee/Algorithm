# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingHG573P-3EW/
def solution(A):
    # write your code in Python 3.6
    left = sum(A)
    right = 0
    min = 1000000000
    A.pop(0)
    for i in reversed(A):
        left -= i
        right += i
        diff = left - right

        if diff < 0:
            diff = -diff

        if min > diff:
            min = diff

    return min
