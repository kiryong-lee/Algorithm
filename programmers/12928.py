
def solution(n):
    _sum = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            _sum += i
            if i != n // i:
                _sum += n // i
    return _sum
