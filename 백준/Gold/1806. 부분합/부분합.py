n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
tmp = arr[0]
ans = int(1e9)
while right < n:
    if tmp < s:
        right += 1
        if right == n:
            break
        tmp += arr[right]
    else:
        ans = min(right-left+1, ans)
        tmp -= arr[left]
        left += 1
    
print(ans) if ans < int(1e9) else print(0)