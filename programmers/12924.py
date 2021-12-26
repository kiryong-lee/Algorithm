
def solution(n):
    count = 1
    nature_list = list(range(n // 2 + 2))
    _sum = 0
    start = 0
    for i, num in enumerate(nature_list):
        _sum += i
        if _sum == n:
            count += 1
        else:
            while _sum > n:
                _sum -= nature_list[start]
                start += 1
            if _sum == n:
                count += 1
    
    return count
