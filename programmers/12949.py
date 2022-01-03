
def solution(arr1, arr2):
    arr3 = [[] for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            _sum = 0
            for k in range(len(arr1[0])):
                _sum += arr1[i][k] * arr2[k][j]
            arr3[i].append(_sum)
            
    return arr3
