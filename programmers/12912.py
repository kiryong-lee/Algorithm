
def solution(a, b):
    if a > b:
        a, b = b, a        
    return (b * (b + 1) - a * (a - 1)) // 2
