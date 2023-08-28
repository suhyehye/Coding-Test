from collections import defaultdict

N, C = map(int, input().split())
M = int(input())
boxes = [list(map(int, input().split())) for _ in range(M)]
boxes.sort(key=lambda x:(x[1], x[0]))

ans = 0
trucks = [0] * (N+1)
for box in boxes:
    x, y, z = box
    for i in range(x,y):
        if trucks[i] + z >= C:
            z = C - trucks[i]
    for i in range(x, y):
        trucks[i] += z
    ans += z
print(ans)