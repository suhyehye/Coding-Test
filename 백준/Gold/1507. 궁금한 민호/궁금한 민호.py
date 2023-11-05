import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
graph = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or j == k or i == k:
                continue
            if arr[i][j] == arr[i][k] + arr[k][j]:
                graph[i][j] = 1
            elif arr[i][j] > arr[i][k] + arr[k][j]:
                print(-1)
                exit()
                
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if not graph[i][j]:
            ans += arr[i][j]

print(ans)