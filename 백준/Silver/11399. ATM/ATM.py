from itertools import accumulate
n = int(input())
arr = sorted(list(map(int, input().split())))
print(sum(accumulate(arr)))