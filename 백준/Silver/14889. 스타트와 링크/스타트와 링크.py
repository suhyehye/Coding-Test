import sys
from itertools import combinations

input = sys.stdin.readline
ans = sys.maxsize

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
people = set([i for i in range(N)])

combs = list(combinations(people, N//2))
for i in combs[:len(combs)//2+1]:
    t1, t2 = 0, 0
    for x in i:
        for y in i:
            t1 += graph[x][y]
    j = people - set(i)
    for x in j:
        for y in j:
            t2 += graph[x][y]
    ans = min(ans, abs(t1-t2))
print(ans)