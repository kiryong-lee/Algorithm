
def solution(n):
    if n == 1:
        return 1
    
    run = [0] * n
    run[0] = 1
    run[1] = 2
    for i in range(2, n):
        run[i] = run[i - 1] + run[i - 2]
    
    return run[-1] % 1234567
