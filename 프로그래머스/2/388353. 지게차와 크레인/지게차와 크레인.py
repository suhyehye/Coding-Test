from collections import deque
def remove_one(storage, x, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if (i==0 or i==n-1 or j==0 or j==m-1) and (visited[i][j] == 0):
                if storage[i][j] == x:
                    storage[i][j] = "."
                    visited[i][j] = 1
                    
                elif storage[i][j] == ".":
                    q = deque([[i,j]])
                    visited[i][j] = 1
                    while q:
                        tmp_x, tmp_y = q.pop()
                        visited[tmp_x][tmp_y] = 1
                        for k in range(4):
                            nx = tmp_x + dx[k]
                            ny = tmp_y + dy[k]
                            if 0 <= nx < len(storage) and 0 <= ny < len(storage[0]) and visited[nx][ny] == 0:
                                if storage[nx][ny] == ".":
                                    visited[nx][ny] = 1
                                    q.append([nx, ny])
                                elif storage[nx][ny] == x:
                                    visited[nx][ny] = 1
                                    storage[nx][ny] = "."
                                    
                    
    return storage
                       
def remove_two(storage, x, n, m):
    ### 예외 처리
    # if len(x) <= 1 or len(x) > 2:
    #     return storage
    # if x[0] != x[1]:
    #     return storage
    for i in range(n):
        for j in range(m):
            if storage[i][j] == x[0]:
                storage[i][j] = "."
    return storage
    
    
def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    for i in range(n):
        storage[i] = list(storage[i])

    for x in requests:
        if len(x) == 1:
            storage = remove_one(storage, x, n, m)
        else:
            storage = remove_two(storage, x, n, m)
    
    cnt = 0
    for x in range(n):
        for y in range(m):
            if storage[x][y] != ".":
                cnt += 1
    return cnt