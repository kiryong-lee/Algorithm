
def solution(N, stages):
    clear = [0] * (N + 2)
    challenge = [0] * (N + 2)
    
    for stage in stages:
        challenge[stage] += 1

    clear[0] = sum(challenge)
    for i in range(1, N + 1):
        clear[i] = clear[i - 1] - challenge[i - 1]
    
    answer = []
    for i in range(1, N + 1):
        if clear[i] == 0:
            answer.append((0, i))
        else:
            answer.append((challenge[i] / clear[i], i))
    
    answer.sort(key=lambda x:(-x[0], x[1]))
    return [y for x, y in answer]
