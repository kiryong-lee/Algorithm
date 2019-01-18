# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training5GA47Q-BZB/
def solution(A):
    # write your code in Python 3.6
    N = len(A)
    peak = []
    for i in range(1, N - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peak.append(i)

    # T == size of peek array
    T = len(peak)
    if T < 3:
        return T
    
    # calculate
    for i in range(2, T + 1):
        count = 1
        current = peak[0]
        for j in range(1, T):
            if peak[j] - current >= i:
                count += 1
                current = peak[j]
                if count >= i:
                    break
        if count < i:
            return i - 1
    
    return T
