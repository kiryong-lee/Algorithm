
def solution(record):
    id_map = {}
    for string in record:
        splited = string.split(' ')
        if splited[0] == 'Enter' or splited[0] == 'Change':
            id_map[splited[1]] = splited[2]
    
    answer = []
    for string in record:
        splited = string.split(' ')
        if splited[0] == 'Enter':
            answer.append(id_map[splited[1]] + "님이 들어왔습니다.")
            
        elif splited[0] == 'Leave':
            answer.append(id_map[splited[1]] + "님이 나갔습니다.")
            
    return answer
