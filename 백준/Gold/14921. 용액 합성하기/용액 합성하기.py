import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

start, end = 0, n-1
ans = int(1e9)

while start < end :
    tmp = arr[start] + arr[end]
    
    if tmp == 0:
        ans = tmp
        break
    elif tmp > 0 :
        if ans > 0:
            ans = min(tmp, ans)
        elif ans * (-1) > tmp:
            ans = tmp
        end -= 1
    else:
        if ans < 0:
            ans = max(tmp, ans)
        elif tmp * (-1) < ans:
            ans = tmp
        start += 1

print(ans)