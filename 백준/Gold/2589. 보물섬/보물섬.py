import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs(x,y):
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    tmp = 1
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'L' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                tmp = max(tmp, visited[nx][ny])
    return tmp - 1

res = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            tmp = bfs(i,j)
            res = max(tmp, res)
print(res)