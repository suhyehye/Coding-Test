N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))

ans, temp = 0, 0
for i in arr:
    if i[0] >= temp:
        temp = i[1]
        ans += 1
print(ans)