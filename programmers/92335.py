
def solution(n, k):
    converted = ''
    while n != 0:
        converted = str(n % k) + converted
        n = n // k
    
    candidates = converted.split('0')
    answer = 0
    for candidate in candidates:
        if candidate == '':
            continue
        
        num = int(candidate)
        if num == 1:
            continue
        
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
        
        if is_prime:
            answer += 1
    
    return answer
