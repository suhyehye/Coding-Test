import sys
from itertools import combinations
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
questions = list(map(int, input().split()))
ans = 0

for i in range(2, N+1):
    for comb in combinations(questions, i):
        if L <= sum(comb) <= R and max(comb) - min(comb) >= X:
            ans += 1
print(ans)   