
def solution(a, b):
    _sum = 0
    for i, j in zip(a, b):
        _sum += i * j
    
    return _sum
