import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
nums = [x for x in range(M)]

ans = 0 
for i in list(combinations(nums, 3)):
    temp = 0
    for x in range(N):
        t = 0
        for y in i:
            t = max(t, arr[x][y])
        temp += t
    ans = max(temp, ans)
print(ans)