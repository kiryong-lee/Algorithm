# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training3U8BYZ-XCB/
def solution(N):
    # write your code in Python 3.6

    arr = []
    idx = 0
    idx_arr = []
    while N > 1:
        binary = N % 2
        arr.append(binary)
        N = N // 2
        if binary == 1:
            idx_arr.append(idx)
        idx += 1
    if N == 1:
        arr.append(1)
        idx_arr.append(idx)

    #print(arr)
    #print(idx_arr)

    max = 0
    for i in range(1, len(idx_arr)):
        if max < idx_arr[i] - idx_arr[i - 1] - 1:
            max = idx_arr[i] - idx_arr[i - 1] - 1

    #print(max)
    return max
