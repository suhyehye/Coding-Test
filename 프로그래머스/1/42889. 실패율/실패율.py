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
    return sorted(count, key=lambda x:count[x], reverse=True)