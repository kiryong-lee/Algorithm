
def solution(d, budget):
    d.sort()
    answer = 0
    for money in d:
        if budget - money >= 0:
            budget -= money
            answer += 1
        else:
            break
    
    return answer
