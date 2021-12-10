
def solution(n):
    answer = 0
    prime_list = [2]
    for number in range(3, n + 1, 2):
        find = False
        sqrt = int(number ** 0.5) + 1
        for prime in prime_list:
            if prime > sqrt:
                break

            if number % prime == 0:
                find = True
                break
        
        if not find:
            prime_list.append(number)
    
    return len(prime_list)
