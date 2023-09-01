N, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [i for i in range(D+1)]

for i in range(D+1):
    if i > 0:
        dp[i] = min(dp[i-1]+1,dp[i])
    for s, e, r in arr:
        if i == s and e <= D and dp[i] + r < dp[e]:
            dp[e] = dp[s] + r
print(dp[D])