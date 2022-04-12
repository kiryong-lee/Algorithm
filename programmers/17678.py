
def time_to_num(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m


def num_to_time(time):
    h, m = divmod(time, 60)
    return '%02d:%02d' % (h, m)


def solution(n, t, m, timetable):
    timetable.sort()
    
    for i in range(n - 1):
        ctime = 540 + i * t
        for j in range(m):
            if timetable and time_to_num(timetable[0]) <= ctime:
                timetable.pop(0)

    last = (n - 1) * t + 540
    if m > len(timetable):
        return num_to_time(last)   
    else:
        pos = m - 1
        candidate = time_to_num(timetable[pos]) - 1
        return num_to_time(min(last, candidate))
