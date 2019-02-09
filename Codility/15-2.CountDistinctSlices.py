# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingPJZWAM-CXM/
def solution(M, A):
    # write your code in Python 3.6
    N = len(A)
    
    if N == 1:
        return 1
    
    flag = [False] * (M + 1)
    result = 0
    start, end, add = 0, 0, 0
    while start < N and end < N:
        a = A[start]
        b = A[end]
        # not appeared then increase add
        if flag[b] == False:
            flag[b] = True
            end += 1
            add += 1
        # appeared then add add to result and decrease add
        else:
            flag[a] = False
            start += 1
            result += add
            add -= 1
    # add remaining
    result += add * (add + 1) // 2
    
    if result > 1000000000:
        result = 1000000000
    
    return result
