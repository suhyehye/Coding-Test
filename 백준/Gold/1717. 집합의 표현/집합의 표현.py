import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
parent = [x for x in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(x, y):
    x, y = find(x), find(y)
    parent[x] = y
    
for _ in range(m):
    k, a, b = map(int, input().split())
    if k == 0:
        union(a, b)
    else:
        a, b = find(a), find(b)
        if a == b:
            print("YES")
        else:
            print("NO")