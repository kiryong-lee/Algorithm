# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training22DKD2-V2K/
def solution(A):
    # write your code in Python 3.6
    B = sorted(A)

    count = 0
    before = -1000001
    for num in B:
        if num != before:
            count += 1
            before = num

    return count
