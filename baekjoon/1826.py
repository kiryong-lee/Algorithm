
import heapq

N = int(input())

gas_station = []
for i in range(N):
    a, b = map(int, input().split())
    gas_station.append((a, b))
gas_station = sorted(gas_station)

L, P = map(int, input().split())

gas_pos = 0
current_go = P
result_count = 0
pq = []
while gas_pos < N:
    if current_go >= L:
        break

    while gas_pos < N and gas_station[gas_pos][0] <= current_go:
        heapq.heappush(pq, -gas_station[gas_pos][1])
        gas_pos += 1

    if pq == []:
        break

    current_go -= heapq.heappop(pq)
    result_count += 1

if current_go >= L:
    print(result_count)
else:
    print(-1)
