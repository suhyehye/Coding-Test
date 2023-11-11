import sys
from collections import defaultdict
input = sys.stdin.readline

f = int(input())

def find(x):
    if f_dict[x]:
        f_dict[x] = find(f_dict[x])
        return f_dict[x]
    return x

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return 
    f_dict[y] = x
    visited[x] += visited[y]

for _ in range(f):
    n = int(input())
    f_dict = defaultdict(set)
    visited = defaultdict(int)
    
    for _ in range(n):
        a, b = input().rstrip().split()
        if a not in f_dict.keys():
            visited[a] = 1
        
        if b not in f_dict.keys():
            visited[b]  = 1
        
        union(a, b)
        print(visited[find(a)])