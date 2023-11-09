import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])

start = 1
end = arr[-1] - arr[0]
ans = 0

while start <= end:
    mid = (end + start) // 2
    temp = arr[0]
    cnt = 1
    
    for i in range(1, len(arr)):
        if arr[i] >= temp + mid : 
            cnt += 1
            temp = arr[i]
    
    if cnt >= c:
        start = mid + 1
        ans = mid 
    
    else:
        end = mid - 1
        
print(ans)