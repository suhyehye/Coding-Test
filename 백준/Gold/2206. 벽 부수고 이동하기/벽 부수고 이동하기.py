import sys
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
# visited[x][y][0] 는 벽 파괴 가능, visited[0][0][1]은 벽 파괴 불가능
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1

    while q:
        x, y, c = q.popleft()
        if x == N-1 and y == M-1 :
            return visited[x][y][c]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[x][y][c]+1
                    q.append([nx,ny,c])
                elif graph[nx][ny] == 1 and c == 0:
                    visited[nx][ny][1] = visited[x][y][c]+1
                    q.append([nx,ny,1])
    return -1
print(bfs())