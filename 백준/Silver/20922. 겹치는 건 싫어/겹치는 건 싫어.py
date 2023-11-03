import sys
from collections import defaultdict 
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
left, right = 0, 0
counter = defaultdict(int)

while right < n:
    if counter[arr[right]] < k:
        counter[arr[right]] += 1
        right += 1
    else:
        counter[arr[left]] -= 1
        left += 1
    ans = max(ans, right-left)

print(ans)