
def solution(numbers):
    n = len(numbers)
    _set = set()
    for i in range(n):
        for j in range(i + 1, n):
            _set.add(numbers[i] + numbers[j])
    
    return sorted(list(_set))
