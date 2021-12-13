
def solution(s, n):
    answer = ''
    for i in range(len(s)):
        asc = ord(s[i])
        if ord('A') <= asc <= ord('Z'):
            asc += n
            if asc > ord('Z'):
                asc -= 26
        elif ord('a') <= asc <= ord('z'):
            asc += n
            if asc > ord('z'):
                asc -= 26
        
        answer += chr(asc)

    return answer
