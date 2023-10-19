from itertools import permutations

n, m = map(int, input().split())
arr = [x for x in range(1, n+1)]

for comb in permutations(arr, m):
    print(*comb)