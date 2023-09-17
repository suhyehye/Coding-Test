import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = sorted([int(input()) for _ in range(n)])

x1, x2 = 0, 1
cnt = 0
ans = arr[-1] - arr[0]
while x1 < n-1 and x2 < n:
    temp = arr[x2] - arr[x1]
    if temp < m :
        x2 += 1
    else:
        ans = min(temp, ans)
        x1 += 1
print(ans)