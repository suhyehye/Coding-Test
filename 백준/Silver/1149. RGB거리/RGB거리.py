N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]

dp[0] = arr[0]
for i in range(1,N):
    for j in range(3):
        dp[i][j] += min([dp[i-1][x] for x in range(3) if x != j]) + arr[i][j]
        
print(min(dp[N-1]))