
from functools import cmp_to_key

def compare(A, B):
    ab = A + B
    ba = B + A    
    if int(ab) - int(ba) > 0:
        return -1
    else:
        return 1


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = cmp_to_key(compare))
    ret = ''.join(numbers)
    while len(ret) > 1 and ret[0] == '0':
        ret = ret[1:]
    
    return ret
