N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    temp  = -1
    for j in range(i):
        if arr[i] > arr[j]:
            temp = max(dp[j], temp)
    dp[i] += temp+1
print(max(dp)+1)