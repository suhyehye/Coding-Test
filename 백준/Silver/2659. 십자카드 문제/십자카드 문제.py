from collections import deque

clock = input().split()

def find(arr):
    temp = int(''.join(arr))
    q = deque(arr)
    for _ in range(3):
        q.rotate(1)
        temp = min(temp, int("".join(q)))
    return temp

cnt = 0
temp = find(clock)
for i in range(1111, temp+1):
    if '0' not in str(i) and i == find(list(str(i))):
        cnt += 1
print(cnt)