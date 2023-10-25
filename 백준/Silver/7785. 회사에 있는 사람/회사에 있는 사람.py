import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = [input().split() for _ in range(n)]
name = defaultdict(int)

for x in arr:
    name[x[0]] += 1

name = sorted(name.items(), reverse=True)

for key, v in name:
    if v % 2 == 1:
        print(key)