import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

ans = 0
stack = []
for idx, x in enumerate(arr):
    while stack and stack[-1] <= x:
        stack.pop()
    stack.append(x)
    ans += len(stack) -1
print(ans)