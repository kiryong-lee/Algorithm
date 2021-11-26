
def solution(n):
    sb = "수박"
    answer = sb * int(n / 2)
    if n % 2 != 0:
        answer += "수"
    return answer
