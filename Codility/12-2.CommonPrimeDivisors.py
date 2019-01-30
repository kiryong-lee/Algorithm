# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingYKJ2RC-2BK/
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def isPrimeDivisor(x, y):
    while x != 1:
        gcd_value = gcd(x, y)
        if gcd_value == 1:
            break
        x //= gcd_value

    return x == 1

def solution(A, B):
    # write your code in Python 3.6
    result = 0
    for a, b in zip(A, B):
        gcd_value = gcd(a, b)
        
        if isPrimeDivisor(a, gcd_value) and isPrimeDivisor(b, gcd_value):
            result += 1
            
    return result
