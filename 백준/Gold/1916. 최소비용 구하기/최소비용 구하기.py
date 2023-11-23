import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [int(1e9)] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])

start, end = map(int, input().split())
visited[start] = 0

q = []
heapq.heappush(q, (0, start))

while q:
    cost, x = heapq.heappop(q)
    if visited[x] < cost:
        continue
    for nx, v in graph[x]:
        n_cost = cost + v
        if n_cost < visited[nx]:
            visited[nx] = n_cost
            heapq.heappush(q, (n_cost, nx))

print(visited[end])