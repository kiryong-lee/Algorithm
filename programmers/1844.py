
xy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def solution(maps):
    n = len(maps[0]) - 1
    m = len(maps) - 1

    length_dict = dict()
    length_dict[(0, 0)] = 1
    stack = [(0, 0)]

    while stack:
        x, y = stack.pop(0)
        
        for xp, yp in xy:
            if 0 <= x + xp <= n and 0 <= y + yp <= m and maps[y + yp][x + xp] == 1:
                if (x + xp, y + yp) not in length_dict:
                    length_dict[(x + xp, y + yp)] = length_dict[(x, y)] + 1
                    stack.append((x + xp, y + yp))

        if (n, m) in length_dict:
            return length_dict[(n, m)]

    return -1
