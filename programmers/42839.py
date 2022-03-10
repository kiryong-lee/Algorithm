
import itertools

def isprime(number):
    if number == 0 or number == 1:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True


def solution(numbers):
    check_dict = dict()
    answer = 0
    for i in range(1, len(numbers) + 1):
        for item in list(itertools.permutations(numbers, i)):
            number = int(''.join(item))
            if number not in check_dict:
                check_dict[number] = number
                
                if isprime(number):
                    answer += 1

    return answer
