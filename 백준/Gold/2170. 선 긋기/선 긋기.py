import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x:(x[0], x[1]))

left, right = arr[0][0], arr[0][1]
ans = 0
for i in range(1, N):
    if arr[i][0] <= right:
        right = max(arr[i][1], right)
    
    else:
        ans += right - left
        left, right = arr[i][0], arr[i][1]

ans += right - left        
print(ans)