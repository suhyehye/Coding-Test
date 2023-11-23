import heapq
from sys import maxsize
def dijkstra(start, n):
    visited = [maxsize] * (n+1)
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, start))
    visited[start] = 0
    
    while q:
        cost, x = heapq.heappop(q)
        if visited[x] < cost:
            continue
        for nx, v in graph[x]:
            n_cost = cost + v
            if n_cost < visited[nx]:
                visited[nx] = n_cost
                heapq.heappush(q, (n_cost, nx))
    return visited
def solution(n, s, a, b, fares):
    answer = maxsize
    global graph
    graph = [[] for _ in range(n+1)]
    
    for x, y, c in fares:
        graph[x].append([y, c])
        graph[y].append([x, c])
    
    v1 = dijkstra(s, n)
    for i in range(1, n+1):
        v2 = dijkstra(i, n)
        answer = min(v1[i] + v2[a] + v2[b], answer)
        
    return answer