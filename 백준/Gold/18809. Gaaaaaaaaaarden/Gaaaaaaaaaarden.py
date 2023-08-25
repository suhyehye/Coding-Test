from collections import deque
from itertools import combinations

N, M, G, R = map(int, input().split())

garden = [list(map(int, input().split())) for _ in range(N)]
broth = []
for i in range(N):
    for j in range(M):
        if garden[i][j] == 2:
            broth.append((i,j))
broth = set(broth)            

def bfs(g_list, r_list):
    cnt = 0
    visited = [[0] * (M) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    
    for x, y in g_list:
        q.append((x,y,'G'))
        visited[x][y] = -1
    for x, y in r_list:
        q.append((x,y,'R'))
        visited[x][y] = 1
    
    while q:
        x, y, c = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and garden[nx][ny] >= 1 and visited[nx][ny] == 0:
                if visited[x][y] < 0:
                    visited[nx][ny] = visited[x][y] -1
                    q.append((nx, ny, c))
                elif 0 < visited[x][y] < 999999:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny,c)) 
            if 0 <= nx < N and 0 <= ny < M and garden[nx][ny] !=0 and visited[nx][ny] + visited[x][y] + 1 == 0:
                visited[nx][ny] = 999999
                cnt += 1
    return cnt   
        
                
ans = 0
for green in list(combinations(broth, G)):
    g_list = list(green)
    diff = list(broth - set(green))
    for red in list(combinations(diff, R)):
        r_list = list(red)
        ans = max(bfs(g_list, r_list), ans)
print(ans)