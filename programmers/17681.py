
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        row = arr1[i] | arr2[i]
        row_str = ''
        while row != 0:
            if row % 2 == 0:
                row_str = " " + row_str
            else:
                row_str = '#' + row_str
            row //= 2
        answer.append(row_str.rjust(n))
            
    return answer
