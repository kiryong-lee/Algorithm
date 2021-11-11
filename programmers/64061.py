
def solution(board, moves):
    board_pos = [0] * len(board[0]) # 각 위치별 깊이 구하기
    height = len(board)
    width = len(board[0])
    for i in range(width):
        for j in range(height):
            if board[j][i] != 0:
                board_pos[i] = j
                break
    
    stack = []
    answer = 0
    for move in moves: # 계산
        pos = move - 1
        if board_pos[pos] < height:
            if stack != [] and stack[-1] == board[board_pos[pos]][pos]:
                stack.pop(-1)
                answer += 2
            else:
                stack.append(board[board_pos[pos]][pos])
            board_pos[pos] += 1  
    
    return answer
