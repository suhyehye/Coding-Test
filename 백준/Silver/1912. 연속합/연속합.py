N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [-1001 for _ in range(N+1)]
for i in range(1,N+1):
    dp[i] = max(arr[i], dp[i-1]+arr[i])

print(max(dp))