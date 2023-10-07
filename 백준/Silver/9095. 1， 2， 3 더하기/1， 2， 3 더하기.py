import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    x = int(input())
    dp = [0] * (x+2)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    
    if x <= 3:
        print(dp[x-1])
        continue
    for i in range(3, x):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[x-1])