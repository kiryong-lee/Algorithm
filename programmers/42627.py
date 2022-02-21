
import heapq

def solution(jobs):
    
    jobs.sort()
    
    current_time = jobs[0][0]
    heap = [[jobs[0][1], jobs[0][0]]]
    time_sum = 0
    i = 1    
    while heap != []:
        work_time, work_start = heapq.heappop(heap)
        time_sum += (current_time - work_start + work_time)
        current_time += work_time
    
        while i < len(jobs) and jobs[i][0] <= current_time:
            heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
            i += 1
            
        if heap == [] and i < len(jobs):
            heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
            current_time = jobs[i][0]
            i += 1
    
    return time_sum // len(jobs)
