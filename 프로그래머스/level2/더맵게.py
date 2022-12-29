import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        h1 = heapq.heappop(scoville)
        h2 = heapq.heappop(scoville)
        s = h1 + h2 * 2
        heapq.heappush(scoville,s)
        answer += 1
        if len(scoville) <= 1 and scoville[0] < K:
            return -1
    return answer
