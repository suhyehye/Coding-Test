import heapq, sys
input = sys.stdin.readline
N = int(input())

l_heap, r_heap = [], []
for i in range(N):
    x = int(input())
    if len(l_heap) == len(r_heap):
        heapq.heappush(l_heap, -x)
    else:
        heapq.heappush(r_heap, x)
    if l_heap and r_heap and -l_heap[0] > r_heap[0]:
        min_v = heapq.heappop(l_heap)
        max_v = heapq.heappop(r_heap)
        heapq.heappush(r_heap, -min_v)
        heapq.heappush(l_heap, -max_v)
    print(l_heap[0] * -1)