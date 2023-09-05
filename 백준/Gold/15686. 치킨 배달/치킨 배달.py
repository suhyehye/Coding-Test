from itertools import combinations
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

chicks = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicks.append((i,j))

ans = int(1e9)
for combs in list(combinations(chicks, M)):
    cnt = 0
    for x in range(N):
        for y in range(N):
            if graph[x][y] == 1:
                temp = int(1e9)
                for i, j in combs:
                    temp = min(temp, abs(x-i)+abs(y-j))
                cnt += temp
    ans = min(ans, cnt)
print(ans)