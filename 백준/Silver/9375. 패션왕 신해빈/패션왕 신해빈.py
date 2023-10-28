import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    items = defaultdict(set)
    for _ in range(n):
        a, b = input().rstrip().split() 
        items[b].add(a)
        
    ans = 1
    for i in items.values():
        ans *= len(i) + 1
    print(ans - 1)