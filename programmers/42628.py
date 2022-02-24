
import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    heap_size = 0
    for operation in operations:
        if operation == "D 1":
            if heap_size > 0:
                heapq.heappop(max_heap)
                heap_size -= 1
                if heap_size == 0:
                    max_heap = []
                    min_heap = []
        elif operation == "D -1":
            if heap_size > 0:
                heapq.heappop(min_heap)
                heap_size -= 1
                if heap_size == 0:
                    max_heap = []
                    min_heap = []
        else:
            insert, number = operation.split(' ')
            number = int(number)
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -number)
            heap_size += 1
    
    if heap_size > 0:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        return [0, 0]
