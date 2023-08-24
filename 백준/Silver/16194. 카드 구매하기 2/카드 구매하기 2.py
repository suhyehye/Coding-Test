import sys
N = int(input())
INF = sys.maxsize

arr = [0] + list(map(int, input().split()))
dp = [INF for _ in range(N+1)]

dp[0] = 0

for i in range(N+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j]+arr[j])

print(dp[N])