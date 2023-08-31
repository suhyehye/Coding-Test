N = int(input())
arr = list(map(int, input().split()))
ans = [0 for _ in range(N)]
stack = []

for i in range(N):
    while stack:
        if stack[-1][1] > arr[i]:
            ans[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, arr[i]])
         
print(*ans)