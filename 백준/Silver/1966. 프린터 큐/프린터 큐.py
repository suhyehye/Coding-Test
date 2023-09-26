import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    q = deque([[idx, x] for idx, x in enumerate(arr)])
    t = 0
    while q:
        idx, x = q.popleft()
        if len(q) == 0:
            t += 1
            print(t)
            break
        for i in list(q):
            if i[1] > x:
                q.append([idx,x])
                break
        else:
            t += 1
            if idx == M:
                print(t)
                break