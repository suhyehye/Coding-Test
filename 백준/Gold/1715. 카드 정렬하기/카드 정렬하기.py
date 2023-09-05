import heapq
N = int(input())
arr = [int(input()) for _ in range(N)]
heapq.heapify(arr)

ans = 0
while len(arr) >= 2:
    a1 = heapq.heappop(arr)
    a2 = heapq.heappop(arr)
    
    ans += a1 + a2
    heapq.heappush(arr, a1+a2)
    
print(ans)