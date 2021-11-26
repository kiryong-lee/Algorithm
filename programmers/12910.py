
def solution(arr, divisor):
    arr.sort()
    answer = []
    for data in arr:
        if data % divisor == 0:
            answer.append(data)
    
    if answer == []:
        return [-1]
    
    return answer
