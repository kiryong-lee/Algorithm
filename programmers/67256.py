

# 각 번호의 좌표
point = [(0, -2), (-1, 1), (0, 1), (1, 1), (-1, 0), (0, 0), (1, 0), (-1, -1), (0, -1), (1, -1), (-1, -2), (1, -2)]

def get_distance(p1, p2):
    return abs(point[p1][1] - point[p2][1]) + abs(point[p1][0] - point[p2][0])

def solution(numbers, hand):
    last_left = 10 # 왼손시작점(-1, -2)
    last_right = 11 # 오른손시작점(1, -2)
    answer = ''
    for number in numbers:
        if number in [1, 4, 7]: # 1, 4, 7 = 왼쪽
            answer += "L"
            last_left = number
        elif number in [3, 6, 9]: # 3, 6, 9 = 오른쪽
            answer += "R"
            last_right = number
        else: # 나머지 = 계산
            left_dist = get_distance(last_left, number)
            right_dist = get_distance(last_right, number)
            if left_dist < right_dist:
                answer += "L"
                last_left = number
            elif right_dist < left_dist:
                answer += "R"
                last_right = number
            else:
                if hand == "left":
                    answer += "L"
                    last_left = number
                else:
                    answer += "R"
                    last_right = number
    
    return answer
