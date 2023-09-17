import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[INF] * N for _ in range(N)]
arr = [[j+1 if i!= j else '-' for j in range(N)] for i in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)
    graph[b-1][a-1] = min(graph[b-1][a-1], c)

for i in range(N):
    graph[i][i] = 0           
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k]+graph[k][j] < graph[i][j]:
                arr[i][j] = arr[i][k]
                graph[i][j] = graph[i][k] + graph[k][j]
for x in arr:
    print(*x)