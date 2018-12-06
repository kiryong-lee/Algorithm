# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training43S6DZ-QCR/
def solution(A):
    # write your code in Python 3.6
    B = sorted(A)

    if B[-1] < 0 or B[0] > 0: # all minus or all plus
        return B[-1] * B[-2] * B[-3]

    if B[0] * B[1] > 0:
        if B[-1] * B[-2] * B[-3] < 0 or B[0] * B[1] > B[-2] * B[-3]:
            return B[0] * B[1] * B[-1]

    return B[-1] * B[-2] * B[-3]
