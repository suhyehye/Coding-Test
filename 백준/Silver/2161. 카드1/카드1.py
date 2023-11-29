from collections import deque
n = int(input())
arr = deque([x for x in range(1, n+1)])
res = []
i = 0

while arr:
    i += 1
    x = arr.popleft()
    
    if i % 2 == 0:
        arr.append(x)
    else:
        res.append(x)

print(*res)