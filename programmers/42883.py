
def solution(number, k):
    n = len(number)
    pos = 0
    for i in range(k):
        while pos < n - 1 and number[pos] >= number[pos + 1]:
            pos += 1
        number = number[:pos] + number[pos + 1:]
        n -= 1
        
        if pos > 0:
            pos -= 1

    return ''.join(number)
