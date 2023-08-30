from collections import deque
N, M, H = map(int, input().split())
tomatos = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]
visited = [[[0] * N for _ in range(M)] for _ in range(H)]

ans = 0
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

q = deque()
for i in range(H):
    for j in range(M):
        for k in range(N):
            if tomatos[i][j][k] == 1:
                visited[i][j][k] = 1
                q.append([i,j,k])

while q:
    x, y, z = q.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < H and 0 <= ny < M and 0 <= nz < N and visited[nx][ny][nz] == 0 and tomatos[nx][ny][nz] == 0:
            q.append([nx, ny, nz])
            tomatos[nx][ny][nz] = tomatos[x][y][z] + 1
            visited[nx][ny][nz] = 1
            
ans = -1
flag = True
for i in range(H):
    for j in range(M):
        for k in range(N):
            if tomatos[i][j][k] == 0:
                ans = -1
                flag = False
                break
            else:
                ans = max(ans, tomatos[i][j][k])
                
if flag == False:
    print(-1)
else:
    print(ans -1)   