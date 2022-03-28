
import itertools

def check_next(place, x, y, first, second):
    nx = x
    ny = y
    nx += first[0]
    ny += first[1]
    if 0 <= nx < 5 and 0 <= ny < 5:
        if place[ny][nx] == 'X':
            return 1
        elif place[ny][nx] == 'P':
            return 0
    else:
        return 1
            
    nx += second[0]
    ny += second[1]
    if 0 <= nx < 5 and 0 <= ny < 5:
        if place[ny][nx] == 'X':
            return 1
        elif place[ny][nx] == 'P':
            return 0
    else:
        return 1
    
    return 1


def check(place, x, y):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for first, second in list(itertools.permutations(directions, 2)):
        if first[0] + second[0] == 0 and first[1] + second[1] == 0:
            if check_next(place, x, y, first, first) == 0:
                return 0
        else:
            if check_next(place, x, y, first, second) == 0:
                return 0
    
    return 1    


def solution(places):    
    answer = []
    for place in places:
        find = False
        for y in range(5):
            for x in range(5):
                if place[y][x] == 'P':
                    if check(place, x, y) == 0:
                        find = True
                        answer.append(0)
                        break
            if find:
                break
        
        if not find:
            answer.append(1)
    
    return answer
