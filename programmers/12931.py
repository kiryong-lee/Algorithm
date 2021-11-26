
def solution(n):
    _sum = 0
    while n > 0:
        _sum += n % 10
        n //= 10

    return _sum
