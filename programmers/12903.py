
def solution(s):
    len_s = len(s)
    k = len(s) // 2
    if len_s % 2 == 0:
        return s[k - 1] + s[k]
    else:
        return s[k]
