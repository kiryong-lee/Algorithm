
def solution(keymap, targets):
    keydict = {}
    
    for keys in keymap:
        for i, key in enumerate(keys, 1):
            if key not in keydict:
                keydict[key] = i
            elif keydict[key] > i:
                keydict[key] = i
    
    result = []
    for target in targets:
        _sum = 0
        for c in target:
            if c in keydict:
                _sum += keydict[c]
            else:
                _sum = -1
                break
        
        result.append(_sum)
    
    return result
