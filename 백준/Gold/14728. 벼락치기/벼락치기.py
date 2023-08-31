import sys
input = sys.stdin.readline
N, T = map(int, input().split())
dp = [0 for _ in range(T+1)]

for i in range(1,N+1):
    w, v = map(int, input().split())
    for j in range(T, w-1, -1):
        dp[j] = max(dp[j], dp[j-w]+v)

print(dp[T])