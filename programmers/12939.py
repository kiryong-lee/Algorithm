
def solution(s):
    int_s = list(map(int, s.split(' ')))
    return str(min(int_s)) + ' ' + str(max(int_s))
