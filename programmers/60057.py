
def solution(s):
    min_len = len(s)        
    for i in range(1, min_len // 2 + 1):
        count = 0
        dup = 1
        j = 0
        while j <= len(s) - i:
            if s[j:j+i] == s[j+i:j+i+i]: # 같으면 중복횟수 증가
                dup += 1
            else:
                if dup != 1: # 같다가 다르면 계산
                    count = count + i + len(str(dup))
                    dup = 1
                else: # 그냥 다르면 더하기
                    count += i
            j += i
        
        if dup != 1: # 검사하다 끝난경우
            count = count + i + len(str(dup))
        
        count = count + len(s) - j # 남은건 붙이기
        
        if min_len > count:
            min_len = count
        
    return min_len
