from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

virus = []
zeros = []
ans = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            zeros.append([i,j])
        elif graph[i][j] == 2:
            virus.append([i,j])

def bfs():
    global ans
    cnt = len(zeros) - 3
    q = deque()
    for i, j in virus:
        q.append((i,j))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and new_graph[nx][ny] == 0:
                new_graph[nx][ny] = 2
                q.append((nx, ny))
                cnt -= 1
    ans = max(ans, cnt)

zero_combs = list(combinations(zeros, 3))
for com in zero_combs:
    new_graph = deepcopy(graph)
    for x, y in com:
        new_graph[x][y] = 1
    bfs()

print(ans)