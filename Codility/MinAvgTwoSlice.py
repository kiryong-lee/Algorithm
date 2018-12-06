# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingBG6B47-GK9/
def solution(A):
    # write your code in Python 3.6
    B = [i for i in A]
    N = len(A)

    C = [0] * N

    min = 1000000000
    min_idx = 0
    for j in range(1, N):
        changed = False
        for i in range(N - j):
            B[i] += A[i + j]
            C[i] = B[i] / (j + 1)

        for i in range(N - j):
            if C[i] < min:
                min = C[i]
                min_idx = i
                changed = True

        if changed == False:
            return min_idx

    return min_idx
