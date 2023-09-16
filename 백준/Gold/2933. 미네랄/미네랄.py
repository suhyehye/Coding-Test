import sys
from collections import deque
from copy import deepcopy
input = lambda: sys.stdin.readline().rstrip()
R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

N = int(input())
arr = list(map(int, input().split()))
            
def bfs(i,j, visited):
    flag = True
    if i == R-1:
        flag = False
    cluster = [[i,j]]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append([i,j])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and graph[nx][ny] == 'x':
                cluster.append([nx,ny])
                q.append([nx,ny])
                visited[nx][ny] = True
                if nx == R-1:
                    flag = False
    return cluster, flag

def cnt_temp(cluster):
    for x, y in cluster:
        graph[x][y] = '.'
        
    temp = 0
    for i in range(1,R):
        for x, y in cluster:
            if x+i+1 == R or graph[x+i+1][y] == 'x':
                temp = i
                return temp


def down(cluster, temp):
    cluster.sort(key=lambda x:x[0], reverse=True)
    for x,y in cluster:
        graph[x+temp][y] = 'x'
    

def find():
    visited = [[False] * (C) for _ in range(R)]
    clusters = []
    t_cluster = None
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'x' and not visited[i][j]:
                visited[i][j] = True
                cluster, flag = bfs(i,j,visited)
                clusters.append(cluster)
                
                if flag and cluster:
                    t_cluster = cluster
                    break
        if t_cluster:
            break
    if t_cluster:
        temp = cnt_temp(cluster)
        down(cluster, temp)
                  
                    
for i in range(N):
    if i % 2 == 0:
        for j in range(C):
            if graph[R-arr[i]][j] == 'x':
                graph[R-arr[i]][j] = '.'
                find()
                break
    else:
        for j in range(C-1,-1,-1):
            if graph[R-arr[i]][j] == 'x':
                graph[R-arr[i]][j] = '.'
                find()
                break
            
for i in graph:
    print(''.join(i))