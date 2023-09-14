import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1
    
q = []
for i in range(1,N+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)
        
arr = []
while q:
    x = heapq.heappop(q)
    arr.append(x)
    for i in graph[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q,i)

print(*arr)