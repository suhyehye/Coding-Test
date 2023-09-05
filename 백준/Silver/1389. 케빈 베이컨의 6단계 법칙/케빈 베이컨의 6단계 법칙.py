import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = 5001
graph = [[INF] * (N) for _ in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i-1][j-1] = 1
    graph[j-1][i-1] = 1

for i in range(N):
    graph[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

cnt = 5001
for i in range(N):
    tmp = 0
    for j in graph[i]:
        tmp += j
    if tmp < cnt:
        cnt = tmp
        ans = i
print(ans+1)