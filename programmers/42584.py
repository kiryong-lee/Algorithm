
def solution(prices):
    stack = []
    end = len(prices)
    ret = [0] * end
    for time, price in enumerate(prices):
        if stack == [] or stack[-1][0] <= price:
            stack.append([price, time])
        else:
            while stack != [] and stack[-1][0] > price:
                top, i = stack.pop()
                ret[i] = time - i
            stack.append([price, time])
        
    while stack != []:
        price, i = stack.pop()
        ret[i] = end - i - 1
    
    return ret
