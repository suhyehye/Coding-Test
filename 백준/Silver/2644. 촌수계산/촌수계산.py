import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# for i in graph:
#     i.sort()
    
def bfs(x, y):
    cnt = 1
    q = deque([x])
    visited[x] = 1
    
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)
            if i == y:
                cnt = visited[x]
                return cnt
    
    if not visited[y]:
        cnt = -1
    return cnt
cnt = bfs(a, b)
print(cnt)