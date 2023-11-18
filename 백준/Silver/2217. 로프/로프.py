import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)])
ans = 0

for idx, x in enumerate(arr):
    tmp = x * (n-idx)
    ans = max(tmp, ans)
print(ans)