
def solution(n, lost, reserve):
        
    common = set(lost).intersection(reserve) # 공통
    
    lost = list(set(lost) - common) # 공통 처리
    reserve = list(set(reserve) - common)
    
    lost.sort()
    reserve.sort()
    
    lost_len = len(lost)
    reserve_len = len(reserve)
    
    lost_pos, reserve_pos = 0, 0
    answer = n - lost_len
    while lost_pos < lost_len and reserve_pos < reserve_len:
        if lost[lost_pos] == reserve[reserve_pos] - 1 \
                or lost[lost_pos] == reserve[reserve_pos] + 1:
            answer += 1
            lost_pos += 1
            reserve_pos += 1
        elif lost[lost_pos] < reserve[reserve_pos]:
            lost_pos += 1
        else:
            reserve_pos += 1

    return answer
