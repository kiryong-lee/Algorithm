# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingWJZCC9-B75/
def solution(A):
    # write your code in Python 3.6
    N = len(A)
    K1 = [0] * N
    K2 = [0] * N
    
    for i, data in enumerate(A[1 : N - 1], start = 1):
        K1[i] = max(K1[i - 1] + data, 0)
    
    for i, data in enumerate(A[N - 2 : 0 : -1], start = 2):
        K2[N - i] = max(K2[N - i + 1] + data, 0)
    
    _max = 0
    for i in range(1, N - 1):
        data = K1[i - 1] + K2[i + 1]
        if data > _max:
            _max = data
    
    return _max
