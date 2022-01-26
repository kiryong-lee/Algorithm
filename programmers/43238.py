
def find_time(start, end, times, n):    
    mid = (start + end) // 2
    handle = 0
    for time in times:
        handle += mid // time
        if handle >= n:
            break
    
    if start == mid and handle >= n:
        return mid
        
    if handle >= n:
        return find_time(start, mid, times, n)
    else:
        return find_time(mid + 1, end, times, n)


def solution(n, times):    
    return find_time(0, max(times) * n, times, n)
