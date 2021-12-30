
def solution(N, road, K):
    nodes = [[] for i in range(N + 1)]
    for r in road:
        nodes[r[1]].append([r[0], r[2]])
        nodes[r[0]].append([r[1], r[2]])
    
    distance = [500001] * (N + 1)
    visited = [False] * (N + 1)
    distance[1] = 0
    queue = [1]
    visited[1] = True
    while queue != []:
        current = queue.pop(0)
        for node in nodes[current]:
            if not visited[node[0]]:
                queue.append(node[0])
                visited[node[0]] = True
            
            if distance[node[0]] > node[1] + distance[current]:
                distance[node[0]] = node[1] + distance[current]
                visited[node[0]] = False

    return sum([1 for d in distance if d <= K])
