import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
ans = []

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
      
print(dp[n])  
while n > 1:
    ans.append(n)
    if n % 3 == 0 and dp[n] == dp[n//3] + 1:
        n = n // 3
    elif n % 2 == 0 and dp[n] == dp[n//2] + 1:
        n = n // 2
    else:
        n = n-1
ans.append(1)
print(*ans)