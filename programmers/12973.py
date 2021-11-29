
def solution(s):
    stack = []
    for c in s:
        if stack == [] or stack[-1] != c:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
    
    if stack == []:
        return 1
    else:
        return 0
