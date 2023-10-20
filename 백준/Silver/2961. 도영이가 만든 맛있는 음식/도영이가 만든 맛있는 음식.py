import sys
input = sys.stdin.readline

n = int(input())
cooks = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
ans = sys.maxsize

def back(idx):
    global ans
    if sum(visited) >= 1:
        t1, t2 = 1, 0
        for i in range(n):
            if visited[i] == 1:
                t1 *= cooks[i][0]
                t2 += cooks[i][1]
        ans = min(ans, abs(t1-t2))
        
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            back(i+1)
            visited[i] = 0

back(0)
print(ans)