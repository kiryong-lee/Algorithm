
def solution(dirs):
    x, y = 0, 0
    point_set = set()
    for d in dirs:
        nx, ny = x, y
        if d == 'U':
            ny += 1
        elif d == 'D':
            ny -= 1
        elif d == 'R':
            nx += 1
        elif d == 'L':
            nx -= 1
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            bx, by = x, y
            x, y = nx, ny
            point_set.add(((x, y), (bx, by)))
            point_set.add(((bx, by), (x, y)))
    
    return len(point_set) // 2
