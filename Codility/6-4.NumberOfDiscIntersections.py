# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training7NENTD-TCP/
def b_search(start, end, arr, value):
    mid = (start + end) // 2
    if start == mid or end == mid:
        return mid
    if arr[mid][0] < value:
        return b_search(mid, end, arr, value)
    elif arr[mid][0] > value:
        return b_search(start, mid, arr, value)
    else:
        while value == arr[mid][0]:
            mid += 1
            if mid >= len(arr):
                return mid - 1
        return mid - 1

def solution(A):

    N = len(A)
    my_list = []
    for i, data in enumerate(A):
        min = i - data
        if min < 0:
            min = 0
        max = i + data
        my_list.append([min, max])

    my_list = sorted(my_list)

    count = 0
    for i in range(N):
        pos = b_search(i, N, my_list, my_list[i][1])
        count += (pos - i)
        if count > 10000000:
            return -1
    return count
