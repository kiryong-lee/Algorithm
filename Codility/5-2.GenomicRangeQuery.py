# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    N = len(S)
    A = [0] * N
    C = [0] * N
    G = [0] * N
    
    if S[0] == 'A':
        A[0] = 1
    elif S[0] == 'C':
        C[0] = 1
    elif S[0] == 'G':
        G[0] = 1
    
    for i in range(1, N):
        A[i] = A[i-1]
        C[i] = C[i-1]
        G[i] = G[i-1]
        
        if S[i] == 'A':
            A[i] = A[i-1] + 1
        elif S[i] == 'C':
            C[i] = C[i-1] + 1
        elif S[i] == 'G':
            G[i] = G[i-1] + 1

    M = len(P)
    ret = []
    for p, q in zip(P, Q):
        if p == 0:
            if A[q] > 0:
                ret.append(1)
            elif C[q] > 0:
                ret.append(2)
            elif G[q] > 0:
                ret.append(3)
            else:
                ret.append(4)
        else:
            minimum = 4
            if G[q] - G[p-1] != 0:
                minimum = 3
            if C[q] - C[p-1] != 0:
                minimum = 2
            if A[q] - A[p-1] != 0:
                minimum = 1
            ret.append(minimum)
        
    return ret
