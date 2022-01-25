
import heapq

def solution(n, works):
    works_heap = []
    for work in works:
        heapq.heappush(works_heap, -work)
    
    for i in range(n):
        work = heapq.heappop(works_heap)
        if work == 0:
            break
        heapq.heappush(works_heap, work + 1)

    return sum([i * i for i in works_heap])
