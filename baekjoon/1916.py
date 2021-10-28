N = int(input())
M = int(input())

city_map = [[100000000] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    i, j, c = map(int, input().split())
    if city_map[i][j] > c:
        city_map[i][j] = c

start, arrive = map(int, input().split())

visited = [False] * (N + 1)
cost = [100000000] * (N + 1)

cost[start] = 0
while visited[arrive] == False:
    lowest_pos = 0
    for i in range(1, N + 1):
        if visited[i] == False and cost[i] < cost[lowest_pos]:
            lowest_pos = i
    
    for i in range(1, N + 1):
        if cost[lowest_pos] + city_map[lowest_pos][i] < cost[i]:
            cost[i] = cost[lowest_pos] + city_map[lowest_pos][i]
    visited[lowest_pos] = True

print(cost[arrive])
