
def solution(a):
    answer = 2
    left_min = a[0]
    for data in a: # 왼쪽 최소
        if data < left_min:
            answer += 1
            left_min = data

    right_min = a[-1]
    for data in reversed(a): # 오른쪽 최소
        if data < right_min:
            answer += 1
            right_min = data
    
    return answer - 1 # 왼쪽 최소, 오른쪽 최소 중복 제거
