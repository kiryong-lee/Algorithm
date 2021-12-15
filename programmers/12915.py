
def solution(strings, n):
    order = [[] for i in range(26)]
    for string in strings:
        order[ord(string[n]) - 97].append(string)
    
    answer = []
    for string in order:
        if string != []:
            answer += sorted(string)
    
    return answer
