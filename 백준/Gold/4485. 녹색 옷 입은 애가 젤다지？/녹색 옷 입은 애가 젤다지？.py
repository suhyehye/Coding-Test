import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra():
    distance[0][0] = graph[0][0]
    q = []
    heapq.heappush(q, (distance[0][0], 0, 0))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        v, x, y = heapq.heappop(q)
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if v + graph[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = v + graph[nx][ny]
                    heapq.heappush(q, (distance[nx][ny], nx, ny))
    
cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    
    dijkstra()
    print(f"Problem {cnt}: {distance[n-1][n-1]}")