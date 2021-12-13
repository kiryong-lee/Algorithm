
def solution(s):
    splited = s.split(' ')
    answer = ''
    for word in splited:
        tmp = ''
        for i in range(len(word)):
            if i % 2 == 0:
                tmp += word[i].upper()
            else:
                tmp += word[i].lower()
        answer += tmp + ' '
    
    return answer[:-1]
