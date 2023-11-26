import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
data = defaultdict(list)

for _ in range(n):
    team = input().rstrip()
    tmp = int(input())
    for _ in range(tmp):
        data[team].append(input().rstrip())

for _ in range(m):
    x = input().rstrip()
    k = int(input())
    
    if k == 1:
        for key, v in data.items():
            if x in v:
                print(key)
                break
    else:
        for i in sorted(data[x]):
            print(i)