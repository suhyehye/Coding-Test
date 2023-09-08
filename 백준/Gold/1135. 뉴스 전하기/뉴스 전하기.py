import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
graph = [[] for _ in range(N)]

for idx, x in enumerate(arr[1:]):
    graph[x].append(idx+1)

dp = [0 for _ in range(N)]

visited = [False] * (N)
q = deque()
q.append(0)
visited[0] = True
ans = 0
def dfs(x):
    time = []
    for i in graph[x]:
        dfs(i)
        time.append(visited[i])
    if not graph[x]:
        time.append(0)
        
    time.sort(reverse=True)
    temp = [time[i] + i + 1 for i in range(len(time))]
    visited[x] = max(temp)

dfs(0)
print(visited[0]-1)