import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
INF = int(1e9)
dist = [INF] * (n+1)
parents = [INF] * (n+1)

def dijkstra():
    dist[1] = 0
    q = []
    heapq.heappush(q, (0, 1))
    
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[0]
            if cost < dist[i[1]]:
                heapq.heappush(q, (cost, i[1]))
                dist[i[1]] = cost
                parents[i[1]] = now
dijkstra()
print(n-1)
for i in range(2,n+1):
    print(i, parents[i])