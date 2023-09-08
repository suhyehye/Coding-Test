from collections import deque
def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j] and maps[i][j] != "X":
                visited[i][j] = True
                temp = int(maps[i][j])
                q = deque()
                q.append([i,j])
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                            if not visited[nx][ny] and maps[nx][ny] != "X":
                                temp += int(maps[nx][ny])
                                q.append([nx,ny])
                                visited[nx][ny] = True
                answer.append(temp)  
    return sorted(answer) if answer != [] else [-1]