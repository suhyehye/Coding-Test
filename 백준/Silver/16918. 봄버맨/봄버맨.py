import sys
from collections import deque
input = sys.stdin.readline

r, c, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
t = 0

def bfs(q):
    while q:
        x, y = q.popleft()
        graph[x][y] = '.'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                graph[nx][ny] = '.'
q = deque()
while t < n:
    t += 1
    if t == 1:
        for i in range(r):
            for j in range(c):
                if graph[i][j] == 'O':
                    q.append([i,j])
        
    elif t%2 == 1:
        bfs(q)
        q = deque()
        for i in range(r):
            for j in range(c):
                if graph[i][j] == 'O':
                    q.append([i,j])

    else:
        graph = [['O'] * c for _ in range(r)]
        
for i in graph:
    print("".join(i))