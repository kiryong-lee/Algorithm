
def solution(arr):
    min_index = 0
    for i in range(len(arr)):
        if arr[min_index] > arr[i]:
            min_index = i
    arr.pop(min_index)
    if arr == []:
        return [-1]
    
    return arr
