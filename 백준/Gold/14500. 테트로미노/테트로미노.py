import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
max_t = max(max(x) for x in graph)

answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, step, total):
    global answer
    # 나머지 탐색 회수가 모두 최대값이어도 현재 최대값보다 작은 경우 탈출
    if total + max_t*(4-step) <= answer:
        return 
    # 4번 모두 탐색한 경우 탈축
    if step == 4:
        answer = max(answer, total)
        return 
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            # ㅏ, ㅓ, ㅜ, ㅗ 탐색
            if step == 2:
                visited[nx][ny] = 1
                dfs(x, y, step+1, total+graph[nx][ny])
                visited[nx][ny] = 0
                
            visited[nx][ny] = 1
            dfs(nx, ny, step+1, total+graph[nx][ny])
            visited[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,1,graph[i][j])
        visited[i][j] = 0

print(answer)