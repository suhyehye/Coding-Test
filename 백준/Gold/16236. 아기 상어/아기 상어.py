import sys
from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def bfs(x, y, s):
    visited = [[0] * N for _ in range(N)]
    dist = [[0] * N for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    fish = []
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 > nx or nx >= N or 0 > ny or ny >= N:
                continue
            if graph[nx][ny] <= s and visited[nx][ny] == 0:
                q.append([nx, ny])
                dist[nx][ny] = dist[x][y] + 1
                visited[nx][ny] = 1
                if 0 < graph[nx][ny] < s:
                    fish.append([nx, ny, dist[nx][ny]])
                
    return sorted(fish, key = lambda x: (-x[2], -x[0], -x[1]))
            
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            graph[i][j] = 0
            x,y = i,j
            break
       
ans, cnt = 0, 0  
s = 2   
while True:
    fish = bfs(x, y, s)
    if len(fish) == 0:
        print(ans)
        break
    
    x, y, d = fish.pop()
    graph[x][y] = 0
    ans += d
    cnt += 1
    
    if cnt == s:
        s += 1
        cnt = 0