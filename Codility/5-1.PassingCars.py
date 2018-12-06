# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training2M36T3-9FP/
def solution(A):
    # write your code in Python 3.6

    right_count = 0
    for i in A:
        if i == 1:
            right_count += 1

    sum = 0
    for i in A:
        if i == 0:
            sum += right_count
            if sum > 1000000000:
                return -1
        else:
            right_count -= 1

    return sum
