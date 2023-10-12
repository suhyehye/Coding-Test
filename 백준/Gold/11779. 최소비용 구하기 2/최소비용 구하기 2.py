import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())

node = [INF] * (n+1)
def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                node[i[0]] = now
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

temp = end
ans = []
while temp != start:
    ans.append(temp)
    temp = node[temp]
ans.append(start) 

print(dist[end])
print(len(ans))
print(*reversed(ans))