
def solution(clothes):
    cdict = {}
    for cloth, ctype in clothes:
        if ctype not in cdict:
            cdict[ctype] = 1
        else:
            cdict[ctype] += 1
    
    clist = list(cdict.values())
    answer = 1
    for i in range(len(clist)):
        answer *= (clist[i] + 1)
    
    return answer - 1
