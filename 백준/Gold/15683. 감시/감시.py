from copy import deepcopy
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
direction = {
    # 0 : 상, 1 : 우, 2 : 하, 3 : 좌
    1 : [[0], [1], [2], [3]],
    2 : [[0,2], [1,3]],
    3 : [[0,1], [1,2], [2,3], [0,3]],
    4 : [[0,1,2], [0,1,3], [0,2,3], [1,2,3]],
    5 : [[0,1,2,3]]
}

cctv = []
for i in range(N):
    for j in range(M):
        if 0 < arr[i][j] < 6:
            cctv.append([i,j,arr[i][j]])
            
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
            
def change(graph,x,y,d):
    for i in d:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            if graph[nx][ny] == 6:
                break
            elif graph[nx][ny] == 0:
                graph[nx][ny] = -1
                
def dfs(depth, graph):
    global ans
    if depth == len(cctv):
        cnt = 0
        for i in range(N):
            cnt += graph[i].count(0)
        ans = min(ans, cnt)
        return ans
    temp = deepcopy(graph)
    x, y, cctv_num = cctv[depth]
    for i in direction[cctv_num]:
        change(temp,x,y,i)
        dfs(depth+1, temp)
        temp = deepcopy(graph)
        
ans = int(1e9)
dfs(0, arr)
print(ans)