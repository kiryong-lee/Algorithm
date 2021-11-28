
import heapq

def solution(scoville, K):
    
    count = 0
    heapq.heapify(scoville)
    while len(scoville) > 0:
        f = heapq.heappop(scoville)
        if f >= K:
            return count
    
        if len(scoville) == 0:
            return -1
        
        s = heapq.heappop(scoville)
        heapq.heappush(scoville, f + s * 2)
        count += 1
    
    return -1
