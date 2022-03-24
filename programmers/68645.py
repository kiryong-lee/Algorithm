
def solution(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2, 3]
    
    arr = [[0] * i for i in range(1, n + 1)]
    num = 1
    row, col = 0, 0
    while arr[row][col] == 0:
        while row < n and arr[row][col] == 0:
            arr[row][col] = num
            num += 1
            row += 1
        row -= 1
        col += 1

        while col < n and arr[row][col] == 0:
            arr[row][col] = num
            num += 1
            col += 1
        col -= 2
        row -= 1

        while row > 0 and col > 0 and arr[row][col] == 0:
            arr[row][col] = num
            num += 1
            row -= 1
            col -= 1
        row += 2
        col += 1

    answer = []
    for i in range(n):
        answer += arr[i]
    
    return answer
