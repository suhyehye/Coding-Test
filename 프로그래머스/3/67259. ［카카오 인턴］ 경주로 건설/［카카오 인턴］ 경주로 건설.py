import heapq
def solution(board):
    answer = 0
    n = len(board)
    visited = [[[int(1e9)] * n for _ in range(n)] for _ in range(4)]
    q = []
    heapq.heappush(q, (0, 0, 0, -1))
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    for i in range(4):
        visited[i][0][0] = 100
    while q:
        v, x, y, d = heapq.heappop(q)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            tmp = 100
            if i != d and d != -1:
                tmp += 500
            if 0 <= nx < n and 0 <= ny < n: 
                if board[nx][ny] != 1 and v+tmp <= visited[i][nx][ny]:
                    heapq.heappush(q, (v+tmp, nx, ny, i))
                    visited[i][nx][ny] = v+tmp
    return min([visited[i][n-1][n-1] for i in range(4)])