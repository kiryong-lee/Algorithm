
def isright(string):
    count = 0
    for c in string:
        if c == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            return False
    
    return True


def change_string(string):
    if string == '':
        return ''
    
    count = 0
    u, v = '', ''
    for c in string:
        if c == '(':
            count += 1
        else:
            count -= 1
        u += c
        if count == 0:
            v = string[len(u):]
            break

    if isright(u):
        return u + change_string(v)
    else:
        u = u[1:-1]
        next_u = ''
        for c in u:
            if c == '(':
                next_u += ')'
            else:
                next_u += '('        
        return '(' + change_string(v) + ')' + next_u


def solution(p):
    return change_string(p)
