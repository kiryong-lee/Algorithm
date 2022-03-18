
def solution(n, cores):
    if n <= len(cores):
        return n

    n -= len(cores)
    low, high = 0, 500000000
    while True:
        mid = (low + high) // 2
        count = 0
        for core in cores:
            count += mid // core
        
        if count >= n:
            high = mid
        else:
            low = mid
    
        if low + 1 == high:
            break
    
    time = low
    n -= sum([time // core for core in cores])
    while True:
        time += 1
        for i, core in enumerate(cores):
            if time % core == 0:
                n -= 1
                if n == 0:
                    return i + 1
