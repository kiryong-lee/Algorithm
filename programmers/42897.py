
def solution(money):
    
    dp1 = []
    dp1.append(money[0])
    dp1.append(max(money[0], money[1]))
    for i in range(2, len(money) - 1):
        if dp1[i - 2] + money[i] > dp1[i - 1]:
            dp1.append(dp1[i - 2] + money[i])
        else:
            dp1.append(dp1[i - 1])
    
    dp2 = [0]
    dp2.append(money[1])
    dp2.append(max(money[1], money[2]))
    for i in range(3, len(money)):
        if dp2[i - 2] + money[i] > dp2[i - 1]:
            dp2.append(dp2[i - 2] + money[i])
        else:
            dp2.append(dp2[i - 1])
    
    return max(dp1[-1], dp2[-1])
