import heapq
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
visited = [False] * (N+1)

q = []
heapq.heappush(q, (0,1))
total = 0

while q:
    cost, now = heapq.heappop(q)
    if visited[now] == False:
        visited[now] = True
        total += cost
        
        for next_cost, next in graph[now]:
            heapq.heappush(q, (next_cost,next))

print(total)