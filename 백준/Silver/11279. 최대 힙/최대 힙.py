import heapq, sys
input = sys.stdin.readline
N = int(input())

heap = []
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, -x)
        continue
    elif len(heap) > 0:
        print(heapq.heappop(heap)*-1)
    else : 
        print(0)