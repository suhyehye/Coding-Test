import sys
from collections import deque
sys.stdin.readline
N, M = map(int, input().split())

graph = [list(input()) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
key = {'a':1, 'b':2, 'c':4, 'd':8, 'e':16, 'f':32}
door = {"A":1, "B":2, "C":4, "D":8, "E":16, "F":32}
            
def bfs(i, j):
    q = deque()
    q.append([i,j,0,0])
    visited[i][j] = 0
    graph[i][j] = '.'
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y, cnt, bit = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != "#":
                if visited[nx][ny] != -1 and visited[nx][ny] | bit == visited[nx][ny]:
                    continue
                visited[nx][ny] = bit
                
                if visited[nx][ny] == -1:
                    visited[nx][ny] = 0
                    
                if graph[nx][ny] == '.':
                    q.append([nx, ny, cnt+1, bit])
                    continue
                
                if graph[nx][ny] == '1':
                    return cnt+1
                
                k = key.get(graph[nx][ny])
                if k != None:
                    q.append([nx, ny, cnt+1, bit|k])
                    continue
                
                d = door.get(graph[nx][ny])
                if d| bit == bit:
                    q.append([nx, ny, cnt+1, bit])
                    
    return -1


for i in range(N):
    for j in range(M):
        if graph[i][j] == '0':
            print(bfs(i,j))
            break
    else:
        continue
    break