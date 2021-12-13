
def solution(phone_number):
    ret = '*' * (len(phone_number) - 4)
    ret += phone_number[-4:]
    return ret
