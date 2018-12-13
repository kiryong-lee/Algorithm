# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingH2RHMM-PAS/
def solution(A, B):
    # write your code in Python 3.6
    
    count = 0
    down_stack = []
    for fish_size, stream in zip(A, B):
        if stream == 0:
            # there's no data in down_stack, increase count
            if len(down_stack) == 0:
                count += 1
            else:
                # remove down_stack while fish in stack is smaller than current fish
                while down_stack[-1] < fish_size:
                    down_stack.pop()
                    # all fishes removed, then increase count
                    if len(down_stack) == 0:
                        count += 1
                        break
        # add fish to down_stack if stream equals 1
        elif stream == 1:
            down_stack.append(fish_size)
    
    return count + len(down_stack)
