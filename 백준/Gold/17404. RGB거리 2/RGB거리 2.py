import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = INF

for i in range(3):
    dp = [[-1, -1, -1] for _ in range(n)]
    dp[0] = [INF, INF, INF]
    dp[0][i] = graph[0][i]
    
    for j in range(1,n):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + graph[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + graph[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + graph[j][2]
    dp[n-1][i] = INF
    ans = min(ans, min(dp[n-1]))
    
print(ans)