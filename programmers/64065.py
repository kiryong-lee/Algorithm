
import re

def solution(s):
    s = s[1:-1]
    matched = re.findall('{(.+?)}', s)
    matched.sort(key=len)
    
    answer = []
    for key in matched:
        candidate = list(map(int, key.split(',')))
        for c in candidate:
            if c not in answer:
                answer.append(c)
    
    return answer
