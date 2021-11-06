
def solution(price, money, count):
    answer = int(count * (count + 1) / 2 * price) - money
    if answer < 0:
        answer = 0
    return answer
