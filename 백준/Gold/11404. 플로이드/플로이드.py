import sys
INF = sys.maxsize

N = int(input())
M = int(input())

dist = [[INF] * (N) for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = min(c, dist[a-1][b-1])
            
for i in range(N):
    for j in range(N):
        for k in range(N):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
            
for i in range(N):
    for j in range(N):
        if dist[i][j] == INF or i == j:
            dist[i][j] = 0
            
for i in dist:
    print(*i)