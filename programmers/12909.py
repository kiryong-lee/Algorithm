
def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack == []:
                return False
            else:
                stack.pop()

    if stack == []:
        return True
    else:
        return False
