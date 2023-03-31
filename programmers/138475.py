import math

def solution(e, starts):
    min_start = min(starts)
    factor_size_list = [0] * 5000001
    for i in range(2, e + 1):
        for j in range(1, min(e // i + 1, i)):
            factor_size_list[i * j] += 2
    for i in range(1, int(e ** 0.5) + 1):
        factor_size_list[i ** 2] += 1

    max_factor_size = 1
    max_factor_number = 1
    for number in range(e, min_start - 1, -1):
        if max_factor_size <= factor_size_list[number]:
            max_factor_size = factor_size_list[number]
            max_factor_number = number
        
        factor_size_list[number] = max_factor_number
    
    answer = [factor_size_list[x] for x in starts]
    
    return answer
