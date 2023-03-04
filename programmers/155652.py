
def solution(s, skip, index):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for x in skip:
        alphabet = alphabet.replace(x, '')

    answer = ''
    n = len(alphabet)
    for c in s:
        answer += alphabet[(alphabet.index(c) + index) % n]   
    
    return answer
