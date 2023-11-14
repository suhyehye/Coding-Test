import sys
input = sys.stdin.readline

n = int(input())
arr = list(int(input()) for _ in range(n))
ans = 0

while len(arr) > 1:
    x = arr.pop()
    if arr[-1] >= x:
        ans += arr[-1] - x + 1
        arr[-1] = x - 1
print(ans)