# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training5FRP4V-5MH/
def solution(A, B, K):
    # write your code in Python 3.6
    ret = B // K - A // K
    if A % K == 0:
        ret += 1

    return ret
