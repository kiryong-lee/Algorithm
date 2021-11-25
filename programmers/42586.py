
import math

def solution(progresses, speeds):
    answer = []
    i, n = 0, len(progresses)
    while i < n:
        day = math.ceil((100 - progresses[i]) / speeds[i])
        complete_count = 0
        continuously = True
        for j in range(i, n):
            progresses[j] = progresses[j] + speeds[j] * day
            if continuously and progresses[j] >= 100:
                complete_count += 1
            else:
                continuously = False
                
        answer.append(complete_count)
        i += complete_count
    
    return answer
