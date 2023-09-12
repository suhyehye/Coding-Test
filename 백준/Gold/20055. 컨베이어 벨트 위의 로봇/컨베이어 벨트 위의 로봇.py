import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = deque(list(map(int, input().split())))
table = deque([0 for _ in range(N*2)])
cnt = 0

def rotate(arr, table):
    arr.rotate(1)
    table.rotate(1)
    table[0] = 0
    table[N-1] = 0

while arr.count(0) < K:
    cnt += 1
    rotate(arr, table)
    for i in range(N-1, 1, -1):
        if table[i-1] == 1 and arr[i] > 0 and table[i] == 0:
            arr[i] -= 1
            table[i] = 1
            table[i-1] = 0
    if arr[0] > 0:
        table[0] = 1
        arr[0] -= 1
print(cnt)