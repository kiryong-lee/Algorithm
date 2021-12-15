
import re

def solution(dartResult):
    score = list(map(int, re.findall(r'\d+', dartResult)))
    pos = 0
    for c in dartResult:
        if c == 'S':
            pos += 1
        elif c == 'D':
            score[pos] **= 2
            pos += 1
        elif c == 'T':
            score[pos] **= 3
            pos += 1
        elif c == '*':
            score[pos - 1] *= 2
            if pos > 1:
                score[pos - 2] *= 2            
        elif c == '#':
            score[pos - 1] = -score[pos - 1]
            
    return sum(score)
	
