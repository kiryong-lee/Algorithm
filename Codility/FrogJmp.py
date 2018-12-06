# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingFRVXKR-4A8/
def solution(X, Y, D):
    # write your code in Python 3.6
    Z = Y - X
    if Z % D == 0:
        return Z // D
    else:
        return Z // D + 1
