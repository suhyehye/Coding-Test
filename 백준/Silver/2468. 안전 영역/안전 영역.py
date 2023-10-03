import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def bfs(x, y, n):
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append([x,y])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and graph[nx][ny] > n:
                q.append([nx, ny])
                visited[nx][ny] = True
    return 1
            
max_h = max(max(x)for x in graph)
ans = 1
for k in range(1, max_h):
    visited = [[False] * N for _ in range(N)]
    temp = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and visited[i][j] == False:
                temp += bfs(i,j,k)
    ans = max(temp, ans)

print(ans)