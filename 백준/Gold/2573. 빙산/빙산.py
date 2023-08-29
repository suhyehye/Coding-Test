from collections import deque
from copy import deepcopy
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
                if graph[nx][ny] == 0 and graph[x][y] >= 1:
                    graph[x][y] -= 1
                elif graph[nx][ny] > 0:
                    q.append([nx, ny])
                    visited[nx][ny] = True
    return 1    

year = 0
while True:
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and visited[i][j] == False:
                cnt += bfs(i,j)
    if cnt >= 2 or cnt == 0:
        break
    year += 1
    
print(year) if cnt >= 2 else print(0)