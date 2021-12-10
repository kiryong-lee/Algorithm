
def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        row = []
        for i in range(len(a)):
            row.append(a[i] + b[i])
        answer.append(row)
    return answer
