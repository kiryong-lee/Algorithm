
def right_bracket(brackets):
    stack = []
    for b in brackets:
        if b == '[' or b == '{' or b == '(':
            stack.append(b)
        else:
            if not stack:
                return False
            
            opposite = stack.pop()
            if opposite == '[' and b == ']':
                pass
            elif opposite == '{' and b == '}':
                pass
            elif opposite == '(' and b == ')':
                pass
            else:
                return False
    
    if stack:
        return False
    
    return True


def solution(s):
    answer = 0
    for i in range(len(s)):
        if right_bracket(s[i:] + s[:i]):
            answer += 1
    
    return answer
