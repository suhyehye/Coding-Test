import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

left, right = 0, k-1
tmp = defaultdict(int)
tmp[c] += 1
answer = 0
for i in range(k):
    tmp[sushi[i]] += 1

while left < n:
    answer = max(len(tmp), answer)

    tmp[sushi[left]] -= 1
    if tmp[sushi[left]] == 0:
        tmp.pop(sushi[left])
    
    left += 1
    right += 1
    tmp[sushi[right % n]] += 1
    
print(answer)