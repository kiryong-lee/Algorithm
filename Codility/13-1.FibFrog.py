# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingWNDSF6-N4F/
def solution(A):
    # write your code in Python 3.6
    # modify A for jump count
    A = [1] + A + [1]
    N = len(A)
    fibo = [0, 1]
    while fibo[-1] + fibo[-2] < N:
        fibo.append(fibo[-1] + fibo[-2])

    B = [-1] * N
    B[0] = 0
    for current in range(N):
        if B[current] != -1:
            # fibo 0 is 0 => useless
            for i in fibo[1:]:
                target = i + current
                # check index bound
                if target >= N:
                    break
                if A[target] == 1:
                    # set minimum jump
                    if B[target] == -1:
                        B[target] = B[current] + 1
                    elif B[target] > B[current] + 1:
                        B[target] = B[current] + 1

    return B[-1]
