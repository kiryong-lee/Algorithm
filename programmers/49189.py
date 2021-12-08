
def solution(n, edge):
    graph = [[] for x in range(n + 1)]
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    visited = [False] * (n + 1)
    distance = [20000] * (n + 1)
    distance[1] = 0
    queue = [1]
    visited[1] = True
    while queue != []:
        target = queue.pop(0)
        for i in graph[target]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
            if distance[i] > distance[target] + 1:
                distance[i] = distance[target] + 1
                
    distance = distance[1:]
    return distance.count(max(distance))
