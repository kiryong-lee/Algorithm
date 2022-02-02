
ret = []

def hanoi(n, fr, by, to):
    if n == 0:
        return
    hanoi(n - 1, fr, to, by)
    ret.append([fr, to])
    hanoi(n - 1, by, fr, to)

def solution(n):
    hanoi(n, 1, 2, 3)
    return ret
