N, M = map(int, input().split())
arr = list(map(int, input().split()))

cnt, interval_sum, end = 0, 0, 0

for i in range(N):
    while end < N and interval_sum<M:
        interval_sum += arr[end]
        end += 1
    if interval_sum == M:
        cnt += 1
    interval_sum -= arr[i]
print(cnt)