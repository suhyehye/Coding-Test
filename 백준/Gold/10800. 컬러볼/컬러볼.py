import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
balls = []

for i in range(n):
    a, b = map(int, input().split())
    balls.append([a,b,i])

balls.sort(key=lambda x:x[1])
res = defaultdict(int)
cum = defaultdict(int)
total = 0
i,j = 0,0

for i in range(n):
    while balls[j][1] < balls[i][1]:
        total += balls[j][1]
        cum[balls[j][0]] += balls[j][1]
        j += 1
    res[balls[i][2]] = total - cum[balls[i][0]]

for i in range(n):
    print(res[i]) 