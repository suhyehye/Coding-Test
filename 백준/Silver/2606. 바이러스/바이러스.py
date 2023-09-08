import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(K):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
ans = 0
visited = [False] * (N+1)
q = deque([1])
visited[1] = True
while q:
    x = q.popleft()
    for i in graph[x]:
        if not visited[i]:
            ans += 1
            visited[i] = True
            q.append(i)
print(ans)