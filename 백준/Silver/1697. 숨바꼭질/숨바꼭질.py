from collections import deque
N, K = map(int, input().split())
dp = [0] * (100002)

q = deque([N])
while q:
    x = q.popleft()
    if x == K:
        print(dp[x])
        break
    for i in (x-1, x+1, x*2):
        if 0 <= i < 100001 and dp[i] == 0:
            dp[i] = dp[x] + 1
            q.append(i)