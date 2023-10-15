import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n)]
visited = [-1] * n

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))

def dfs(x, temp):
    for i, d in graph[x]:
        if visited[i] == -1 :
            visited[i] = temp + d
            dfs(i, temp+d)
            
visited[0] = 0
dfs(0, 0)

start = visited.index(max(visited))
visited = [-1] * n
visited[start] = 0
dfs(start, 0)
print(max(visited))