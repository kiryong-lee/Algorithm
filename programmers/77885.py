
def solution(numbers):
    answer = []
    for number in numbers:
        binary = bin(number)[2:]
        b_list = list(binary)
        n = len(b_list)
        found = False
        for i in range(n): # 0을 1로 바꾸되 1번째 이상에선 그 전 숫자를 0으로 변경
            if b_list[n - i - 1] == '0':
                b_list[n - i - 1] = '1'
                if i != 0:
                    b_list[n - i] = '0'
                found = True
                break
        
        if not found: # 찾지 못하면 맨 앞 수를 0, 그리고 앞에 1 붙임
            b_list[0] = '0'
            b_list = ['1'] + b_list    
            
        answer.append(int(''.join(b_list), 2))
    
    return answer
