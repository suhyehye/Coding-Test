import heapq
def solution(n, works):
    works.sort(reverse=True)
    works = [-x for x in works if x>0]
    for i in range(n):
        w = heapq.heappop(works)
        if w <= -1:
            heapq.heappush(works,w+1)
        else:
            heapq.heappush(works,w)
        
    return sum([x**2 for x in works])
