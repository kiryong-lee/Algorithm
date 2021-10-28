def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()

    zero_count = 0
    min_count = 0
    lottos_pos = 0
    win_nums_pos = 0
    while lottos_pos < 6 and lottos[lottos_pos] == 0:
        lottos_pos += 1

    zero_count = lottos_pos    
    while lottos_pos < 6 and win_nums_pos < 6:
        if lottos[lottos_pos] < win_nums[win_nums_pos]:
            lottos_pos += 1
        elif lottos[lottos_pos] == win_nums[win_nums_pos]:
            lottos_pos += 1
            win_nums_pos += 1
            min_count += 1
        else:
            win_nums_pos += 1

    return [min(7 - min_count - zero_count, 6), min(7 - min_count, 6)]
