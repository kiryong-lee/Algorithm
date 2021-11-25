
import math

def solution(left, right):
    _sum = 0
    for number in range(left, right + 1):
        count = 0
        for i in range(1, math.ceil(number ** 0.5) + 1):
            if number % i == 0:
                count += 2
                if i * i == number:
                    count -= 1
                    
        if count % 2 == 0:
            _sum += number
        else:
            _sum -= number
    
    return _sum
