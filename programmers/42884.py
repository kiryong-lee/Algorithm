
def solution(routes):
    routes.sort()    
    print(routes)
    
    i, n = 0, len(routes)
    count = 0
    while i < n:
        right = routes[i][1]
        j = i + 1
        while j < n and routes[j][0] <= right:
            right = min(right, routes[j][1])
            j += 1
        
        count += 1
        i = j
    
    return count
