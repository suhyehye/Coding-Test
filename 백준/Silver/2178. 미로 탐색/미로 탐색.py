import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

q = deque()
q.append([0,0])
graph[0][0] = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append([nx, ny])
print(graph[N-1][M-1] + 1)