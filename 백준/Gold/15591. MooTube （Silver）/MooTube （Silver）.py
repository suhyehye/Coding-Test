import sys
from collections import deque

input = sys.stdin.readline
N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q,r))
    graph[q].append((p,r))
    
def bfs(start):
    visited = [0] * (N+1)
    q = deque([start])
    visited[start] = 1
    cnt = 0
    while q:
        x = q.popleft()
        for i,j in graph[x]:
            if visited[i] == 0 :
                if j >= k:
                    visited[i] = 1
                    q.append(i)
                    cnt += 1
    return cnt
    
    
for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(v))