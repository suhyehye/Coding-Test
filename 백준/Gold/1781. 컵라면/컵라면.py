import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)])
   
q = []
for deadline, cup in arr:
    heapq.heappush(q, cup)
    if deadline < len(q):
        heapq.heappop(q)
        
print(sum(q))