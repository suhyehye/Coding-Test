import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]*101 for _ in range(101)]
direction = [(0,1), (-1,0), (0,-1), (1,0)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    arr[y][x] = 1
    temp = [d]
    for _ in range(g):
        n_temp = []
        for i in range(len(temp)-1, -1, -1):
            ni = (temp[i]+1) % 4
            n_temp.append(ni)
        temp.extend(n_temp)
    
    for i in temp:
        ny, nx = y+direction[i][0], x+direction[i][1]
        arr[ny][nx] = 1
        x, y = nx, ny

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j+1] == 1:
            cnt += 1
            
print(cnt)