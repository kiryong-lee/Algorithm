
import time
import math

def solution(fees, records):
    in_dict = dict()
    result_dict = dict()
    
    # 입출차 처리
    for s in records:
        t, cnumber, inout = s.split(' ')
        tt = time.strptime(t, '%H:%M')
        int_time = tt.tm_min + tt.tm_hour * 60
        
        if inout == 'IN':
            in_dict[cnumber] = int_time
        else:
            if cnumber in result_dict:
                result_dict[cnumber] = result_dict[cnumber] + int_time - in_dict[cnumber]
            else:
                result_dict[cnumber] = int_time - in_dict[cnumber]
            in_dict.pop(cnumber)

    # 출차 안된 차 처리
    for cnumber, int_time in in_dict.items():
        if cnumber in result_dict:
            result_dict[cnumber] = result_dict[cnumber] + 23 * 60 + 59 - in_dict[cnumber]
        else:
            result_dict[cnumber] = 23 * 60 + 59 - in_dict[cnumber]
    
    result = list(result_dict.items())
    result.sort()
    
    # 돈 계산
    answer = []
    for cnumber, itime in result:
        if itime - fees[0] > 0:
            answer.append(math.ceil((itime - fees[0]) / fees[2]) * fees[3] + fees[1])
        else:
            answer.append(fees[1])   
    
    return answer
