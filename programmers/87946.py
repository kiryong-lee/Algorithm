
from itertools import permutations

def solution(k, dungeons):
    dungeon_perm = permutations(dungeons)
    answer = 0
    for dungeon_list in list(dungeon_perm):
        limit = k
        current_clear = 0
        for dungeon in dungeon_list:
            if limit >= dungeon[0]:
                limit -= dungeon[1]
                current_clear += 1

        if answer < current_clear:
            answer = current_clear
    
    return answer
