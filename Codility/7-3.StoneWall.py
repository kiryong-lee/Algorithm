# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingW959AA-UM2/
def solution(H):
    # write your code in Python 3.6
    count = 1
    stack = [H[0]]
    for data in H:
        # if recent data is smaller than current data
        if data > stack[-1]:
            # push the data to stack and increase count
            stack.append(data)
            count += 1
        # if recent data is larger than current data
        elif data < stack[-1]:
            recent = stack.pop()
            # pop from the stack while stacked data are larger than current data
            while recent > data:
                if len(stack) == 0:
                    break
                recent = stack.pop()
            count += 1
            # push recent data
            if data > recent:
                stack.append(recent)
            # decrease the count when current data equals recent data
            elif data == recent:
                count -= 1
            # push current data to stack
            stack.append(data)

    return count
