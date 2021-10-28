xList = [1, 0, -1, 0]
yList = [0, 1, 0, -1]

N, M = map(int, input().split())
iceberg = []
for i in range(N):
    iceberg.append(list(map(int, input().split())))

year = 0
while True:
    year += 1
    
    for i in range(N - 1):
        for j in range(M - 1):
            if iceberg[i][j] > 0:
                for k in range(4):
                    if iceberg[i + xList[k]][j + yList[k]] == 0:
                        iceberg[i][j] -= 1
                if iceberg[i][j] <= 0:
                    iceberg[i][j] = 0
                    if iceberg[i + 1][j] != 0:
                        iceberg[i + 1][j] += 1
                    if iceberg[i][j + 1] != 0:
                        iceberg[i][j + 1] += 1

    connected = 0
    check = [[0] * M for i in range(N)]
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] > 0 and check[i][j] == 0:
                connected += 1
                if connected > 1:
                    print(year)
                    exit()
                
                check[i][j] = 1
                xyList = []
                xyList.append([i, j])
                while xyList != []:
                    x, y = xyList.pop()
                    for k in range(4):
                        ex = x + xList[k]
                        ey = y + yList[k]
                        if 0 < ex < N and 0 < ey < M and iceberg[ex][ey] > 0 and check[ex][ey] == 0:
                            check[ex][ey] = 1
                            xyList.append([ex, ey]);
    
    if connected == 0:
        print(0)
        exit()
