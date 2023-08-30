import sys
N, K = map(int, input().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
ans = 0
while K > 0:
    coin = coins.pop()
    if K >= coin:
        ans += K // coin
        K = K % coin
print(ans)