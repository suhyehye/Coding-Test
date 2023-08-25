n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
dp = [1] + [0] * (k+1)

for a in arr:
    for b in range(a, k+1):
        dp[b] += dp[b-a]
print(dp[k])