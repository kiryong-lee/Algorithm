
import math

def solution(n,a,b):
    if a > b:
        a, b = b, a

    answer = 1
    while b - a != 1 or math.ceil(a / 2) != math.ceil(b / 2):
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        answer += 1

    return answer
