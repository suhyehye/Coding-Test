from collections import deque
M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]

q = deque()
for x in range(N):
    for y in range(M):
        if tomatos[x][y] == 1:
            q.append([x,y])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and tomatos[nx][ny] == 0:
            tomatos[nx][ny] = tomatos[x][y] + 1
            q.append([nx,ny])

ans = 0
Break = True
for x in range(N):
    for y in range(M):
        if tomatos[x][y] == 0:
            ans = 0
            Break = False
            break
        else:
            ans = max(tomatos[x][y], ans)
    if Break == False:
        break
print(ans-1)