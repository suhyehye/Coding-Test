import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
wolf, sheep = 0, 0

def find(x, y):
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    
    temp_w, temp_s = 1, 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0 and graph[nx][ny] != '#':
                visited[nx][ny] = 1
                q.append((nx, ny))
                
                if graph[nx][ny] == 'v':
                    temp_w += 1
                elif graph[nx][ny] == 'o':
                    temp_s += 1
    if temp_s > temp_w:
        temp_w = 0
    else:
        temp_s = 0
    return temp_s, temp_w

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'v' and visited[i][j] == 0:
            s, w = find(i,j)
            sheep += s
            wolf += w

for i in range(r):
    for j in range(c):
        if visited[i][j] == 0 and graph[i][j] == 'o':
            sheep += 1

print(sheep, wolf)