import sys
input = sys.stdin.readline

INF = 10**9+7

N, M = map(int, input().split())
graph = [[0] * M for _ in range(N)]
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = -1
    
odd = [(1,-1), (1,0), (0,1)]
even = [(0,1), (1,1), (1,0)]
graph[0][0] = 1
for x in range(M):
    for y in range(N):
        if graph[y][x] == -1:
            continue
        for i in range(3):
            if x % 2 == 0:
                nx, ny = x + odd[i][0], y + odd[i][1]
            else:
                nx, ny = x + even[i][0], y + even[i][1]
                
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] != -1:
                graph[ny][nx] += graph[y][x] % INF      
print(graph[N-1][M-1] % INF)