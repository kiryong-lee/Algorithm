
def get_parent(link, x):
    if link[x] == -1:
        return -1
    
    xp = x
    while link[xp] != xp:
        xp = link[xp]
    return xp


def solution(n, costs):
    costs.sort(key = lambda costs : costs[2])
    link = [-1] * n
    
    total = 0
    for x, y, cost in costs:
        if x > y:
            x, y = y, x
            
        xp = get_parent(link, x)
        yp = get_parent(link, y)
        if xp == -1 and yp == -1:
            link[x] = x
            link[y] = x
            total += cost
        elif xp == -1:
            link[x] = x
            link[yp] = x
            total += cost
        elif yp == -1:
            link[y] = x
            total += cost
        else:
            if xp != yp:
                link[yp] = xp
                total += cost
        
    return total
