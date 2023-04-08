def solution(plans):
    
    plans = list(map(lambda x : [x[0], x[1], int(x[2])], plans))
    plans.sort(key = lambda x : x[1])
    plans.append(['x', '23:59', 1440])
    
    stack = []
    answer = []
    current_plan = plans[0]
    for next_plan in plans[1:]:
        remain_time = current_plan[2] - get_diff_time(current_plan[1], next_plan[1])
        if remain_time > 0:
            current_plan[2] = remain_time
            stack.append(current_plan)
        elif remain_time == 0:
            answer.append(current_plan[0])
        else:
            answer.append(current_plan[0])
            while stack != [] and remain_time < 0:
                last_plan = stack.pop()
                remain_time += last_plan[2]
                if remain_time <= 0:
                    answer.append(last_plan[0])
                else:
                    last_plan[2] = remain_time
                    stack.append(last_plan)
        
        current_plan = next_plan
    
    while stack != []:
        answer.append(stack.pop()[0])
    
    return answer


def get_finish_time(current_plan):
    current_h, current_m = map(int, current_plan[1].split(":"))
    current_m += current_plan[2]
    current_h += current_m // 60
    current_m %= 60
    
    return str(current_h) + ":" + str(current_m)


def get_diff_time(current_time, next_time):
    next_h, next_m = map(int, next_time.split(":"))
    current_h, current_m = map(int, current_time.split(":"))
    
    return (next_h - current_h) * 60 + next_m - current_m
