
total = 0

def find_queen(queen, n, pos):
    global total
    if pos == n:
        total += 1
        return
    
    for i in range(n):
        queen[pos] = i + 1
        check = True
        for j in range(pos):
            if queen[pos] == queen[j] or abs(queen[pos] - queen[j]) == abs(pos - j):
                check = False
                break
                
        if check:
            find_queen(queen, n, pos + 1)

def solution(n):
    queen = [0] * n
    find_queen(queen, n, 0)
    
    return total
