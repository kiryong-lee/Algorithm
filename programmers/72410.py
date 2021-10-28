import re

def solution(new_id):
    legal = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    new_id = new_id.lower()
    
    answer = ''
    for c in new_id:
        if c in legal:
            answer += c
    
    answer = re.sub(r'\.+', '.', answer)
    
    if answer[0] == '.':
        answer = answer[1:]
    if answer != '' and answer[-1] == '.':
        answer = answer[0:-1]
    
    if answer == '':
        answer = 'a'
        
    if len(answer) > 15:
        answer = answer[0:15]
    
    
    if answer[-1] == '.':
        answer = answer[0:-1]
    
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer
