
def dfs(numbers, target, index, _sum):
    if index == len(numbers):
        if _sum == target:
            return 1
        else:
            return 0
    
    result = 0
    result += dfs(numbers, target, index + 1, _sum + numbers[index])
    result += dfs(numbers, target, index + 1, _sum - numbers[index])
        
    return result
    

def solution(numbers, target):    
    return dfs(numbers, target, 0, 0)
