# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training9HUZQ2-4DY/
def solution(N, M):
    # write your code in Python 3.6
    # get gcd to a
    a, b = N, M
    while b:
        a, b = b, a % b

    return N // a
