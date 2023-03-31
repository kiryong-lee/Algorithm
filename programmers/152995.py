
def solution(scores):

    wanho = scores[0]
    
    scores.sort(key=lambda s: (-s[0], s[1]))
    
    max_score = scores[0][1]
    answer = 1
    for score in scores:
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1
        
        if max_score <= score[1]:
            if sum(wanho) < sum(score):
                answer += 1
            max_score = score[1]
        
    return answer
