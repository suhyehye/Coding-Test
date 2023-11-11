from collections import Counter
def solution(N, stages):
    total = len(stages)
    count = dict()
    for x in range(1, N+1):
        if total > 0:
            tmp = stages.count(x)
            count[x] = tmp / total
            total -= tmp
        else:
            count[x] = 0
    count = sorted(count.items(), key = lambda x:x[1], reverse=True)
    return [x[0] for x in count]