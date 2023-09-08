import sys
from collections import deque, defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
N, M, V = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
for i in graph.keys():
    graph[i].sort()
    
d_visited = [False] * (N+1)
def dfs(x):
    d_visited[x] = True
    print(x, end=" ")
    for i in graph[x]:
        if not d_visited[i]:
            dfs(i)

def bfs(x):
    visited = [False] * (N+1)
    print(x, end=" ")
    
    q = deque()
    q.append(x)
    visited[x] = True
    while q:
        i = q.popleft()
        for v in graph[i]:
            if not visited[v]:
                print(v, end=" ")
                q.append(v)
                visited[v] = True

dfs(V)
print("")
bfs(V)