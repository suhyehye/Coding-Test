import sys
input = sys.stdin.readline
INF = sys.maxsize

N, V = map(int, input().split())
graph = [[INF] * (N) for _ in range(N)]

for _ in range(V):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c

    
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                
ans = INF
for i in range(N):
    ans = min(ans, graph[i][i])

print(ans) if ans != INF else print(-1)