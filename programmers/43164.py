
def traverse(tickets, visited, answer):
    if len(answer) == len(tickets) + 1:
        return True
    
    for i, ticket in enumerate(tickets):
        if visited[i] == False and ticket[0] == answer[-1]:
            visited[i] = True
            answer.append(ticket[1])
            if traverse(tickets, visited, answer):
                return True
            
            visited[i] = False
            answer.pop()
    
    return False


def solution(tickets):
    tickets.sort()
    visited = [False] * len(tickets)
    answer = ['ICN']
    traverse(tickets, visited, answer)

    return answer
