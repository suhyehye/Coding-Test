import sys
import heapq
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    K = int(input())
    arr = list(map(int, input().split()))
    heapq.heapify(arr)
    temp = 0
    while True:
        i = heapq.heappop(arr)
        j = heapq.heappop(arr)
        temp += i+j
        heapq.heappush(arr, i+j)
        if len(arr) == 1:
            print(temp)
            break