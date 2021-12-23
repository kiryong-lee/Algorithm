
def get_count(a):
    count = 0
    while a > 0:
        b = a % 2
        a //= 2
        if b == 1:
            count += 1
    return count

def solution(n):
    count_1 = get_count(n)
    while True:
        n += 1
        count_2 = get_count(n)
        if count_1 == count_2:
            return n
