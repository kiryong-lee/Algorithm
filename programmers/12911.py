
def get_count(a):
    count = 0
    while a > 0:
        b = a % 2
        a //= 2
        if b == 1:
            count += 1
    return count
