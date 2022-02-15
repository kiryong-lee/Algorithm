
def solution(rows, columns, queries):
    num = 1
    mylist = []
    mylist.append([])
    for i in range(rows):
        a = [-1]
        for j in range(columns):
            a.append(num)
            num += 1
        mylist.append(a)
    
    answer = []
    for query in queries:
        tmp_num = mylist[query[0]][query[1]]
        min_num = tmp_num
        
        for i in range(query[0], query[2]):
            mylist[i][query[1]] = mylist[i + 1][query[1]]
            min_num = min(min_num, mylist[i][query[1]])
            
        for i in range(query[1], query[3]):
            mylist[query[2]][i] = mylist[query[2]][i + 1]
            min_num = min(min_num, mylist[query[2]][i])

        for i in range(query[2], query[0], -1):
            mylist[i][query[3]] = mylist[i - 1][query[3]]
            min_num = min(min_num, mylist[i][query[3]])
        
        for i in range(query[3], query[1], -1):
            mylist[query[0]][i] = mylist[query[0]][i - 1]
            min_num = min(min_num, mylist[query[0]][i])
        
        mylist[query[0]][query[1] + 1] = tmp_num
        answer.append(min_num)
    
    return answer
