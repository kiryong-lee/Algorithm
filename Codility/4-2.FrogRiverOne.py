# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingTGCQSY-BPY/
def solution(X, A):
    # write your code in Python 3.6
    if len(A) < X:
        return -1

    B = [False] * (X + 1)
    B[0] = True
    frog_position = 0
    for i in range(len(A)):
        if B[A[i]] == False:
            B[A[i]] = True
            while frog_position < X and B[frog_position + 1] == True:
                frog_position += 1

            if frog_position == X:
                return i

        B[A[i]] = True

    return -1
