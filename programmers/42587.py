
def solution(priorities, location):
    priority_count = [0] * 10
    target_priority_list = list(enumerate(priorities))
    current_max = 0
    for priority in priorities:
        priority_count[priority] += 1
        if current_max < priority:
            current_max = priority

    print_count = 0
    while True:
        target, priority = target_priority_list.pop(0)
        if priority == current_max:
            print_count += 1
            if target == location:
                return print_count
            priority_count[current_max] -= 1
            while priority_count[current_max] == 0:
                current_max -= 1
        else:
            target_priority_list.append((target, priority))
    
    return -1
