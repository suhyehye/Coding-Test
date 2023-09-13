import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
def bfs():
    q = deque([0])
    visited[0] = 1
    while q:
        x = q.popleft()
        for i in arr[x]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
        
        
for _ in range(T):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n+2)]
    arr = [[] for _ in range(n+2)]
    visited = [0] * (n+2)
    for i in range(n+1):
        for j in range(i+1,n+2):
            if abs(graph[i][0] - graph[j][0]) + abs(graph[i][1]-graph[j][1]) <= 20*50:
                arr[i].append(j)
                arr[j].append(i)
    bfs()
    print("happy") if visited[n+1] == 1 else print("sad")