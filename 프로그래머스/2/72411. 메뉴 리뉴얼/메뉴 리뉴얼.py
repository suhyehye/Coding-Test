from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    orders = [list(x) for x in orders]
    for c in course:
        tmp = defaultdict(int)
        for order in orders:
            if len(order) >= c:
                combs = combinations(order, c)
                for com in combs:
                    tmp[''.join(sorted(com))] += 1
        if not tmp:
            continue
        max_k = max(tmp.values())
        if max_k > 1:
            answer.extend([k for k, v in tmp.items() if v == max_k])
    return sorted(answer)