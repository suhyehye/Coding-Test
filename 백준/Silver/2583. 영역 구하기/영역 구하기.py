import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[j][i] = 1

visited = [[False] * N for _ in range(M)]
cnt = 0
ans = []

def bfs(x, y):
    temp = 1
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    q = deque()
    q.append([x,y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                visited[nx][ny] = True
                q.append([nx, ny])
                temp += 1
    return temp

for x in range(M):
    for y in range(N):
        if not visited[x][y] and graph[x][y] == 0:
            visited[x][y] = True
            ans.append(bfs(x,y))
            cnt += 1
print(cnt)
print(*sorted(ans))