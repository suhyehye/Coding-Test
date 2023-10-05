import sys

input = sys.stdin.readline
N, C = map(int, input().split())
house = sorted([int(input()) for _ in range(N)])

start = 1
end = house[-1] - house[0]
ans = 0

while start <= end:
    mid = (start + end) // 2
    temp = house[0]
    cnt = 1
    
    for i in range(1, len(house)):
        if house[i] >= temp + mid:
            cnt += 1
            temp = house[i]
            
    if cnt >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)