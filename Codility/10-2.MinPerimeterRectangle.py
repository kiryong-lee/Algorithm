# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingK7AXT3-WHN/
def solution(N):
    # write your code in Python 3.6
    _N = int(N**(1/2))
    A = 0
    for i in range(1, _N + 1):
        if N % i == 0:
            A = i

    if A * A == N:
        return A * 4
    
    B = N // A
    return (A + B) * 2
