import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

visited = [[0] * m for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y, tmp):
    visited[x][y] = 1
    tmp.append([x, y])
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(nx, ny, tmp)
    else:
        return tmp

ans = 0
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1 and not visited[x][y]:
            tmp = dfs(x, y, [])
            ans = max(ans, len(tmp))
            
print(ans)