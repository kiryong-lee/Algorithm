
import datetime

def solution(lines):
    # 시작, 종료 계산 쉬운 형태로 변경
    start_list = []
    end_list = []
    for data in lines:
        day, start, duration = data.split(' ')
        end = datetime.datetime.strptime(start, "%H:%M:%S.%f").timestamp() * 1000
        end_list.append(end)
        start_list.append(end - float(duration[0:-1]) * 1000)
        
    max_tps = 1
    for i in range(len(end_list)):
        # 끝이 시작보다 앞이거나, 시작이 끝과 연결되어 있으면 tps에 포함
        current_tps = 1
        for j in range(i + 1, len(start_list)):
            if end_list[i] >= start_list[j]:
                current_tps += 1
            elif start_list[j] - end_list[i] < 999:
                current_tps += 1
            
        if max_tps < current_tps:
            max_tps = current_tps
    
    return max_tps
