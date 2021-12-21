
import math

def solution(arr):
    lcm = arr[0]
    for number in arr[1:]:
        lcm = lcm * number // math.gcd(lcm, number)
    
    return lcm
