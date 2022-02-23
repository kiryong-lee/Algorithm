
def solution(genres, plays):
    
    order = dict()
    for g, p in zip(genres, plays):
        if g in order:
            order[g] += p
        else:
            order[g] = p
    
    answer = []
    while len(order) != 0:
        genre = max(order, key=order.get)
        f, s = -1, -1
        for i, g in enumerate(genres):
            if genre == g:
                if f == -1:
                    f = i
                elif plays[f] >= plays[i]:
                    if s == -1 or plays[s] < plays[i]:
                        s = i
                elif plays[f] < plays[i]:
                    s = f
                    f = i
        answer.append(f)
        if s != -1:
            answer.append(s)      
        
        del(order[genre])
    
    return answer
