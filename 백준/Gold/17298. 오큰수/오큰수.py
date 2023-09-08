N = int(input())
arr = list(map(int, input().split()))

stack = []
ans = [-1 for _ in range(N)]
for idx, x in enumerate(arr):
    while stack and stack[-1][1] < x:
        ans[stack.pop()[0]] = x
    stack.append((idx,x))
print(*ans)