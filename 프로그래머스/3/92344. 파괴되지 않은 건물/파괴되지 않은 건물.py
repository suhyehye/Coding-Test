def solution(board, skill):
    data = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    for s in skill:
        typ, r1, c1, r2, c2, degree = s
        if typ == 1: typ = -1
        if typ == 2: typ = 1
        
        data[r1][c1] += typ * degree
        data[r1][c2+1] -= typ * degree
        data[r2+1][c1] -= typ * degree
        data[r2+1][c2+1] += typ * degree
        
    for i in range(len(data)):
        for j in range(1, len(data[0])):
            data[i][j] += data[i][j-1]
    
    for j in range(len(data[0])):
        for i in range(1, len(data)):
            data[i][j] += data[i-1][j]
        
    ans = 0
    for i in range(len(board)) : 
        for j in range(len(board[0])) :
            if board[i][j] + data[i][j] > 0:
                ans += 1  
    return ans