
def solution(answers):
    first = (1, 2, 3, 4, 5)
    second = (2, 1, 2, 3, 2, 4, 2, 5)
    third = (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    
    right = [0, 0, 0]
    for i, d in enumerate(answers):
        if d == first[i % 5]:
            right[0] += 1
        if d == second[i % 8]:
            right[1] += 1
        if d == third[i % 10]:
            right[2] += 1
    
    high = max(right)
    answer = []
    for i, score in enumerate(right, start=1):
        if high == score:
            answer.append(i)
    
    return answer
