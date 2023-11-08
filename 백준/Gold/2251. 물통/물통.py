from collections import deque

a, b, c = map(int, input().split())

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = 1
        q.append((x, y))

def bfs():
    while q:
        x, y = q.popleft()
        z = c - x - y
        
        if x == 0:
            answer.append(z)
        
        tmp = min(x, b-y)
        pour(x-tmp, y+tmp)
        
        tmp = min(x, c-z)
        pour(x-tmp, y)
        
        tmp = min(a-x, y)
        pour(x+tmp, y-tmp)
        
        tmp = min(y, c-z)
        pour(x, y-tmp)
        
        tmp = min(a-x, z)
        pour(x+tmp, y)
        
        tmp = min(z, b-y)
        pour(x, y+tmp)
        
q = deque()
q.append((0, 0))

visited = [[0] * (b+1) for _ in range(a+1)]
visited[0][0] = 1

answer = []
bfs()
answer.sort()
print(*answer)