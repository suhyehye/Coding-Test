import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[100000000] * N for _ in range(N)]

for _ in range(N-1):
    x, y, d = map(int, input().split())
    graph[x-1][y-1] = d
    graph[y-1][x-1] = d
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
            
for _ in range(M):
    x, y = map(int, input().split())
    print(graph[x-1][y-1])