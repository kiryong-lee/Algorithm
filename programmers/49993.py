
def solution(skill, skill_trees):
    possible = 0
    
    for skill_tree in skill_trees:
        order = ''
        for s in skill_tree:
            if s in skill:
                order += s
            
            if len(order) == len(skill):
                break
            
        if order == skill[:len(order)]:
            possible += 1
    
    return possible
