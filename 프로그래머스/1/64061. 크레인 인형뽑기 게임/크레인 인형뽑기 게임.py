def solution(board, moves):
    bucket = []
    cnt = 0
    for move in moves:
        for i in range(len(board[0])):
            if board[i][move-1] > 0:
                if bucket and bucket[-1] == board[i][move-1]:
                    cnt += 2
                    board[i][move-1] = 0
                    bucket.pop()
                else:
                    bucket.append(board[i][move-1])
                    board[i][move-1] = 0
                break
    return cnt