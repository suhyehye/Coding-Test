import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
arr = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a-1].append([b-1,c])

def dijkstra(start):
    dist = [INF] * N
    q = []
    heapq.heappush(q,(0, start))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i in arr[now]:
            if d + i[1] < dist[i[0]]:
                dist[i[0]] = d+i[1]
                heapq.heappush(q, (d+i[1], i[0]))
    return dist

ans = 0   
back = dijkstra(X-1)             
for i in range(N):
    if i != X-1:
        start = dijkstra(i)
        ans = max(start[X-1]+back[i], ans)
print(ans)