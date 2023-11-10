import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
cost = list(map(int, input().split()))
graph = [set() for _ in range(n)]
visited = [0 for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    if a == b:
        continue
    graph[a-1].add(b-1)
    graph[b-1].add(a-1)

def bfs(x):
    visited[x] = 1
    q = deque()
    q.append(x)
    tmp = set([x])
    
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                tmp.add(i)
                q.append(i)
                visited[i] = 1
    
    c_tmp = cost[x]
    for i in tmp:
        c_tmp = min(c_tmp, cost[i])
    return c_tmp

ans = 0
for i in range(n):
    if not visited[i]:
        ans += bfs(i)
        
print(ans) if ans <= k else print("Oh no")