import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
data = sorted([list(map(int, input().split())) for _ in range(n)])
bags = sorted([int(input()) for _ in range(k)])
ans = 0
heap = []

for x in bags:
    while data and data[0][0] <= x:
        heapq.heappush(heap, -data[0][1])
        heapq.heappop(data)
    
    if heap:
        ans -= heapq.heappop(heap)
        
print(ans)