# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingTR69S8-JGP/
def solution(N, A):
    # write your code in Python 3.6
    max = 0
    min = 0
    B = [0] * (N + 1)

    for i in A:
        if i > N:
            min = max
        else:
            if B[i] < min:
                B[i] = min + 1
            else:
                B[i] += 1
            if B[i] > max:
                max = B[i]

    for i in range(1, N + 1):
        if B[i] < min:
            B[i] = min
    B.pop(0)
    return B
