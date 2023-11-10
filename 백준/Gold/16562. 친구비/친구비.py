import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))
parents = [x for x in range(n+1)]

def find(x: int) -> int:
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x:int, y:int) -> None:
    x, y = find(x), find(y)
    
    if cost[x] < cost[y]:
        parents[y] = x
    else:
        parents[x] = y
        
        
for _ in range(m):
    v, w = map(int, input().split())
    union(v, w)
        
friends = set()    
ans = 0

for i in range(1, n+1):
    if find(i) not in friends:
        ans += cost[parents[i]]
        friends.add(parents[i])

print(ans) if ans <= k else print("Oh no")