
import math

def solution(begin, end):
    block = []
    if begin == 1:
        block.append(0)
        begin += 1
    for number in range(begin, end + 1):
        prime = True
        for s in range(2, int(math.sqrt(number)) + 1):
            if number % s == 0:
                candidate = number // s
                if candidate <= 10000000:
                    prime = False
                    block.append(candidate)
                    break
                    
        if prime:
            block.append(1)
        
    return block
