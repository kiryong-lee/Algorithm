# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training9BU528-7PZ/
def solution(A):
    # write your code in Python 3.6

    A = sorted(A)
    min = 1

    if A[-1] < 1:
        return min

    for i in A:
        if i == min:
            min += 1
        elif i > min:
            return min

    return min
