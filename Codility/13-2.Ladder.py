# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    max_A = max(A)
    N = len(A)
    
    if max_A == 1:
        return [1] * N
    
    rung = [0, 1, 2] + [0] * (max_A - 2)
    max_mod = 2 ** 30
    for i in range(3, max_A + 1):
        rung[i] = (rung[i - 1] + rung[i - 2]) % max_mod
    
    result = [0] * N
    for i in range(N):
        result[i] = rung[A[i]] % (2 ** B[i])
        # print(A[i], B[i], rung[A[i]], 2 ** B[i])
    return result
