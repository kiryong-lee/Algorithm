# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingY3WADW-CZT/
def b_search(start, end, arr, val):
    middle = (start + end) // 2
    if start == middle or end == middle:
        return middle
    if arr[middle] < val:
        return b_search(middle, end, arr, val)
    elif arr[middle] > val:
        return b_search(start, middle, arr, val)
    else:
        return middle

def solution(S, P, Q):
    # write your code in Python 3.6
    A, C, G = [], [], []
    N = len(S)
    for i in range(N):
        if S[i] == 'A':
            A.append(i)
        elif S[i] == 'C':
            C.append(i)
        elif S[i] == 'G':
            G.append(i)

    M = len(P)
    ret = [4] * M
    for i in range(M):
        if len(A) > 0:
            _P = b_search(0, len(A), A, P[i])
            _Q = b_search(0, len(A), A, Q[i])
            _mid = (_P + _Q) // 2
            if P[i] <= A[_mid] and A[_mid] <= Q[i]:
                ret[i] = 1
                continue

        if len(C) > 0:
            _P = b_search(0, len(C), C, P[i])
            _Q = b_search(0, len(C), C, Q[i])
            _mid = (_P + _Q) // 2
            if P[i] <= C[_mid] and C[_mid] <= Q[i]:
                ret[i] = 2
                continue

        if len(G) > 0:
            _P = b_search(0, len(G), G, P[i])
            _Q = b_search(0, len(G), G, Q[i])
            _mid = (_P + _Q) // 2
            if P[i] <= G[_mid] and G[_mid] <= Q[i]:
                ret[i] = 3
                continue

    return ret
