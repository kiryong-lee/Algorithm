# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingJZRTFC-6P2/
def binary_search(start, end, arr):
    if start + 1 == end:
        return start
    if arr[(start + end) // 2] == (start + end) // 2:
        return binary_search((start + end) // 2, end, arr)
    else:
        return binary_search(start, (start + end) // 2, arr)

def solution(A):
    # write your code in Python 3.6

    B = sorted(A)
    B.insert(0, 0)
    N = len(B)

    result = B[binary_search(0, N, B)]

    return  result + 1
