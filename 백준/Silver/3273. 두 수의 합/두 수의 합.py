import sys
input = sys.stdin.readline

n = int(input())
data = sorted(map(int, input().split()))
x = int(input())

res = 0
left, right = 0, n-1
while left < right and right < n:
    if data[left] + data[right] == x:
        res += 1
        left += 1
    elif data[left] + data[right] < x:
        left += 1
    else:
        right -= 1

print(res)