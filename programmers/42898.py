
def solution(m, n, puddles):
    
    mymap = [[0] * m for i in range(n)]
    mymap[0][0] = 1
    for x, y in puddles:
        mymap[y - 1][x - 1] = -1
    
    for i in range(1, m):
        if mymap[0][i] != -1:
            mymap[0][i] = mymap[0][i - 1]
        else:
            mymap[0][i] = 0
    
    for i in range(1, n):
        if mymap[i][0] != -1:
            mymap[i][0] = mymap[i - 1][0]
        else:
            mymap[i][0] = 0

    for i in range(1, n):
        for j in range(1, m):
            if mymap[i][j] == -1:
                mymap[i][j] = 0
            else:
                mymap[i][j] = (mymap[i - 1][j] + mymap[i][j - 1]) % 1000000007
            
    return mymap[n - 1][m - 1]
