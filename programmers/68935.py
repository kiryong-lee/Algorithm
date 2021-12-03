
def solution(n):
    ternary = ''
    while n > 2:
        a = n // 3
        b = n % 3
        ternary = str(b) + ternary
        n = a
    if n != 0:
        ternary = str(n) + ternary
    
    answer = 0
    for i, value in enumerate(ternary):
        if value != '0':
            answer += 3 ** i * int(value)
    
    return answer
