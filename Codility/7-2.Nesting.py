# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingD9QCMU-N9M/
def solution(S):
    # write your code in Python 3.6

    stack = []
    for bracket in S:
        if bracket == '(':
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return 0
            item = stack.pop()

    if len(stack) > 0:
        return 0

    return 1
