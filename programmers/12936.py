
digit = [0, 1]

def solution(n, k):
    people = [i + 1 for i in range(n)]
    for i in range(2, n):
        digit.append(digit[i - 1] * i)
    
    result = []
    for i in range(n - 1, 0, -1):
        index = 0
        while k - digit[i] > 0:
            k -= digit[i]
            index += 1
        
        result.append(people[index])
        people.pop(index)
    
    result += people
    
    return result
