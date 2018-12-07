# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingF5X2CV-393/
def solution(S):
    # write your code in Python 3.6

    stack = []
    for bracket in S:
        if bracket == '{' or bracket == '[' or bracket == '(':
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return 0
            item = stack.pop()
            if item == '{':
                if bracket != '}':
                    return 0
            elif item == '[':
                if bracket != ']':
                    return 0
            else:
                if bracket != ')':
                    return 0

    if len(stack) > 0:
        return 0

    return 1
