n, m, l = map(int, input().split())
arr = [0] + sorted(list(map(int, input().split()))) + [l]

start = 1
end = l-1
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] >= mid:
            cnt += (arr[i] - arr[i-1] - 1) // mid
    
    if cnt <= m:
        ans = mid
        end = mid - 1
    
    else:
        start = mid + 1
            
print(ans)