
def solution(sticker):
    n = len(sticker) - 1
    if n < 3:
        return max(sticker)
    
    dp1 = [sticker[0], max(sticker[0], sticker[1])]
    for i, num in enumerate(sticker[2:-1], start = 2):
        dp1.append(max(dp1[i - 2] + num, dp1[i - 1]))
    
    dp2 = [sticker[1], max(sticker[1], sticker[2])]
    for i, num in enumerate(sticker[3:], start = 2):
        dp2.append(max(dp2[i - 2] + num, dp2[i - 1]))
    
    return max(dp1[-1], dp2[-1])
