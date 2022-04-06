
def convert(n, b):
    T = '0123456789ABCDEF'
    q, r = divmod(n, b)
    return convert(q, b) + T[r] if q else T[r]


def solution(n, t, m, p):
    number = ''
    for i in range(t * m):
        number += convert(i, n)
    
    answer = ''
    position = p - 1
    while len(answer) < t:
        answer += number[position]
        position += m
    
    return answer
