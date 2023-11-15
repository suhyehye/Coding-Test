from collections import deque
def check(x, y, board, m, n):
    remove = set()
    tmp = board[x][y]
    if board[x+1][y] == tmp and board[x][y+1] == tmp and board[x+1][y+1] == tmp:
        remove = [(x,y), (x+1,y), (x,y+1), (x+1,y+1)]
    return remove

def remove_blocks(remove, board):
    remove = sorted(remove, key=lambda x:x[0])
    for x, y in remove:
        for i in range(x, 0, -1):
            board[i][y] = board[i-1][y]
        
        board[0][y] = 0
    return board

def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]

    while 1:
        remove = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]:
                    tmp = check(i,j, board, m, n)
                    if tmp:
                        remove.update(tmp)
                        
        if not remove:
            break

        answer += len(remove)
        board = remove_blocks(remove, board)
        
    return answer