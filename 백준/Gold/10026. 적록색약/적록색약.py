from collections import deque
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color):
    q = deque()
    q.append([x,y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == color and visited[nx][ny] == False : 
                q.append([nx,ny])
                visited[nx][ny] = True


cnt1, cnt2 = 0, 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i,j,graph[i][j])
            visited[i][j] = True
            cnt1 += 1

# Green을 Red로 변환 (적록색맹)
for i in range(N):
    for j in range(N):
        if graph[i][j] == "G":
            graph[i][j] = "R"

visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i,j,graph[i][j])
            visited[i][j] = True
            cnt2 += 1
print(cnt1, cnt2)