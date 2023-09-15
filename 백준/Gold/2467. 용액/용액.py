import sys
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

x1, x2 = 0, N-1
total = sys.maxsize
ans = []
while x1 < x2:
    temp = arr[x1] + arr[x2]
    
    if abs(temp) < total:
        total = abs(temp)
        ans = [arr[x1], arr[x2]]
    if temp > 0:
        x2 -= 1
    elif temp < 0:
        x1 += 1
    else:
        break
print(*ans)