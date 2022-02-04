
def solution(s):
    iterate_count = 0
    total_zero_count = 0    
    while s != '1':
        zero_count = s.count('0')
        total_zero_count += zero_count
        iterate_count += 1
        
        s = '1' * (len(s) - zero_count)
        s = bin(len(s))[2:]    
    
    return [iterate_count, total_zero_count]
