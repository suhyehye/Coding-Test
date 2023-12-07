import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split())
data = [0] + list(map(int, input().split()))

graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for i in range(n+1):
    graph[i][i] = 0
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            
res = 0
for i in range(1, n+1):
    tmp = 0
    for j in range(1, n+1):
        if graph[i][j] <= m :
            tmp += data[j]
    res = max(tmp, res)

print(res)