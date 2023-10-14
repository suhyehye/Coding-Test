import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    combs = sorted(set(combinations(arr[1:], 6)))
    for com in combs:
        print(*com)
    print()