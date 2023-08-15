from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a,b):
    q = deque()
    q.append([a,b])
    graph[a][b] = 0
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                q.append([nx, ny])    
    return cnt

w = 0
ans = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            ans += 1
            w = max(w, bfs(i,j))
            
print(ans)
print(w)