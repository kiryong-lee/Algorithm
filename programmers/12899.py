
def solution(n):
    answer = ''
    while n > 2:
        a = n // 3
        b = n % 3
        if b == 0:
            a -= 1
            answer = '4' + answer
        else:
            answer = str(b) + answer
        n = a
    
    if n != 0:
        answer = str(n) + answer
    
    return answer
