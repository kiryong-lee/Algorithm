
def solution(n):
    if n % 2 == 1:
        return 2

    for i in range(3, n + 1, 2):
        if n % i == 1:
            return i
