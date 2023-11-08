import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

graph = [list(input().rstrip().split()) for _ in range(5)]
ans = set()

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, tmp):
    tmp += graph[x][y]
    if len(tmp) == 6:
        ans.add(tmp)
        return
        
    else:
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < 5 and 0 <= ny < 5:
                dfs(nx, ny, tmp)
    return 

for x in range(5):
    for y in range(5):
        dfs(x, y, '')

print(len(ans))