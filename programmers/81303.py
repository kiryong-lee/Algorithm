
def solution(n, k, cmd):
    deleted_stack = []
    mylist = [[i - 1, i + 1] for i in range(n)]
    mylist[-1][1] = -1
    
    for c in cmd:
        if c[0] == 'U':
            move_count = int(c.split(' ')[1])
            for i in range(move_count):
                k = mylist[k][0]
        
        elif c[0] == 'D':
            move_count = int(c.split(' ')[1])
            for i in range(move_count):
                k = mylist[k][1]
        
        elif c[0] == 'C':
            deleted_stack.append(k)
            before = mylist[k][0]
            after = mylist[k][1]
            
            mylist[before][1] = after
            if after != -1:
                mylist[after][0] = before
                k = after
            else:
                k = before
                
        elif c[0] == 'Z':
            before = mylist[deleted_stack[-1]][0]
            after = mylist[deleted_stack[-1]][1]
            
            mylist[before][1] = deleted_stack[-1]
            if after != -1:
                mylist[after][0] = deleted_stack[-1]
            
            deleted_stack.pop(-1)
        
    ret = ['O'] * n
    for deleted in deleted_stack:
        ret[deleted] = 'X'
    
    return "".join(ret)
