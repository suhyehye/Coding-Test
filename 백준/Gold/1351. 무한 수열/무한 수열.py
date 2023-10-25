from collections import defaultdict

n, p, q = map(int, input().split())
data = defaultdict(int)
data[0] = 1

def solution(n):
    if data[n] != 0:
        return data[n]
    else:
        data[n] = solution(n//p) + solution(n//q)
        return data[n]

print(solution(n))