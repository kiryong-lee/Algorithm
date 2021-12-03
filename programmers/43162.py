

def solution(n, computers):
    linked = [False] * n
    count = 0
    for i in range(n):
        if linked[i] == True:
            continue

        queue = [i]
        count += 1
        while queue != []:
            target = queue.pop(0)
            for j in range(n):
                if j == target:
                    continue
                if computers[target][j] == 1 and linked[j] == False:
                    queue.append(j)
                    linked[j] = True

    return count
