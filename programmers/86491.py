
def solution(sizes):
    w_max = 0
    h_max = 0
    for w, h in sizes:
        if w < h: # 가로를 항상 더 길게
            t = w
            w = h
            h = t
                
        if w_max < w: # 최대 비교
            w_max = w
        if h_max < h:
            h_max = h
    
    return w_max * h_max
