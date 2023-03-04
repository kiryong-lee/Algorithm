
def solution(wallpaper):
    lux, luy = 50, 50
    rdx, rdy = 0, 0
    
    for x, line in enumerate(wallpaper):
        for y in range(len(line)):
            if line[y] == '#':
                if lux > x:
                    lux = x
                if rdx < x + 1:
                    rdx = x + 1
                if luy > y:
                    luy = y
                if rdy < y + 1:
                    rdy = y + 1
    
    return [lux, luy, rdx, rdy]
