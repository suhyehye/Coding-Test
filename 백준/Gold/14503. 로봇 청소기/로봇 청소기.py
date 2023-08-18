import sys
input = sys.stdin.readline
N, M = map(int, input().split())

x, y, d = map(int, input().split())

walls = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1
visited[x][y] = 1

while True:
    c = 0
    for _ in range(4):
        nx = x + dx[(d+3)%4]
        ny = y + dy[(d+3)%4]
        d = (d+3) % 4
        if 0 <= nx < N and 0 <= ny < M and walls[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                x, y = nx, ny
                c = 1
                break
                
    if c == 0:
        if walls[x - dx[d]][y - dy[d]] == 1:
            print(cnt)
            break
        else:
            x,y = x - dx[d], y - dy[d]