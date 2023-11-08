import sys
from collections import defaultdict
input = sys.stdin.readline

data = defaultdict(list)
n = int(input())

for i in range(1, n+1):
    data[int(input())].append(i)
    
visited = [0] * (n+1)
ans = []

def dfs(x, tmp):
    visited[x] = 1
    tmp.add(x)
    
    for i in data[x]:
        if i not in tmp:
            dfs(i, tmp.copy())
        else:
            ans.extend(list(tmp))
            return

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, set([]))
        
ans.sort()
print(len(ans))
for i in ans:
    print(i)