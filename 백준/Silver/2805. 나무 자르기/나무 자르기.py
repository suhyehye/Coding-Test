import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)
ans = 0

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    
    for tree in trees:
        if tree > mid:
            tmp += tree - mid
    
    if tmp >= m:
        ans = max(mid, ans)
        start = mid + 1
    else:
        end = mid - 1

print(ans)