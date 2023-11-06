from collections import deque
n, k = map(int, input().split())
dp = [-1] * 100002

q = deque([n])
dp[n] = 0

if n >= k:
    print(n-k)
    exit()
    
while q:
    x = q.popleft()
    if x == k:
        print(dp[x])
        break
    if 0 <= 2 * x < 100001 and dp[2*x] == -1:
        dp[2*x] = dp[x]
        q.appendleft(2*x)
        
    if 0 <= x - 1 < 100001 and dp[x-1] == -1:
        q.append(x-1)
        dp[x-1] = dp[x] + 1
    
    if 0 <= x + 1 < 100001 and dp[x+1] == -1:
        q.append(x+1)
        dp[x+1] = dp[x] + 1