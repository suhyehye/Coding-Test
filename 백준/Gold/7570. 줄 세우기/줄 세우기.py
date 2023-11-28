n = int(input())
nums = list(map(int, input().split()))
idx = [-1] * (n+1)

for i, x in enumerate(nums):
    idx[x] = i

cnt = 0
tmp = 1

for x in range(1, n):
    if idx[x] < idx[x+1]:
        tmp += 1
    else:
        cnt = max(tmp, cnt)
        tmp = 1

print(n - cnt if n != 1 else 0)