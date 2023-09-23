import sys
from collections import deque

T = int(input())

def bfs(x, y):
    q = deque()
    q.append([x,y])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = 1


for _ in range(T):
    M, N, K = map(int, input().split())
    cnt = 0
    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j)
                cnt += 1
    print(cnt)