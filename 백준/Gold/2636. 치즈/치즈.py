from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    q = deque()
    q.append([0,0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    cnt = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    visited[nx][ny] =  True
                    cnt += 1
    return cnt

time = -1
ans = []
while 1:
    time += 1
    cnt = bfs()
    ans.append(cnt)
    if cnt == 0:
        print(time)
        print(ans[-2])
        break