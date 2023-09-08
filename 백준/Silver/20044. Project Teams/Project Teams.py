from collections import deque
N = int(input())
arr = deque(sorted(list(map(int, input().split()))))

ans = 10**9
while arr:
    x1, x2 = arr.popleft(), arr.pop()
    ans = min(ans, x1+x2)
print(ans)