import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:(x[0], x[1]))
res = [q[0][1]]

for x in q[1:]:
    if x[0] < res[0] :
        heapq.heappush(res, x[1])
    else:
        heapq.heappop(res)
        heapq.heappush(res, x[1])

print(len(res))