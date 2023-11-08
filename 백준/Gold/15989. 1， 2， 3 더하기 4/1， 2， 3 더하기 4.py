import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x = int(input())
    dp = [1] * 10001
    dp[2] = 2
    dp[3] = 3
    
    for i in range(4, x+1):
        dp[i] += i//2 + dp[i-3]
    print(dp[x])