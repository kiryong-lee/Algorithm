
def solution(skill, skill_trees):
    possible = 0
    
    for skill_tree in skill_trees:
        i, j = 0, 0
        order = ''
        while j < len(skill_tree):
            if skill_tree[j] in skill:
                order += skill_tree[j]
            
            if len(order) == len(skill):
                break
            
            j += 1
        
        if order == skill[:len(order)]:
            possible += 1
    
    return possible
