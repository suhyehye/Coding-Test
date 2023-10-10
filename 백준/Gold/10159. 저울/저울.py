import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())

arr = [[0]*N for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1
for i in range(N):
    cnt = -1
    for j in range(N):
        if arr[i][j] == 0 and arr[j][i] == 0:
            cnt += 1
    print(cnt)