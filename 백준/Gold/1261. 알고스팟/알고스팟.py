from collections import deque

M, N = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]            

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[-1] * M for _ in range(N)]
answer = 0

q = deque()
q.append([0,0])
visited[0][0] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]
                    q.appendleft([nx,ny])
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])        
print(visited[N-1][M-1])