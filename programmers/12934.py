
def solution(n):
    sqrt_n = int(n ** 0.5)
    if sqrt_n ** 2 == n:
        return (sqrt_n + 1) ** 2
    else:
        return -1
