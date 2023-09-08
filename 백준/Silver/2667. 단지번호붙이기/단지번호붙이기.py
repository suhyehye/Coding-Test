import sys
from collections import deque

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0
ans = []
def bfs(x,y):
    temp = 1
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] != 0:
                q.append([nx,ny])
                visited[nx][ny] = True
                temp += 1
    return temp
                        
for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] != 0:
            ans.append(bfs(i,j))
            cnt += 1
print(cnt)
for v in sorted(ans):
    print(v)