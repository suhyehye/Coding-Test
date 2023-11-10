n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())

start = 1
end = arr[-1]
ans = 0

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    
    for i in arr:
        tmp += min(i, mid)
    
    if tmp > m:
        end = mid - 1
    else:
        start = mid + 1
        ans = mid
        
print(ans)