# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingPGB4M7-5FP/
def is_valid(A, K, M):
    
    block_sum = 0
    block_count = 0
    
    for i in A:
        
        if block_sum + i > M:
            block_sum = i
            block_count += 1
        else:
            block_sum += i
        
        if block_count >= K:
            return False
            
    return True

def solution(K, M, A):
    # write your code in Python 3.6
    low = max(A)
    high = sum(A)
    
    if K == 1:
        return high
    elif K >= len(A):
        return low
    
    while low <= high:
        mid = (low + high) // 2
        
        if is_valid(A, K, mid):
            high = mid - 1
        else:
            low = mid + 1
    
    return low
