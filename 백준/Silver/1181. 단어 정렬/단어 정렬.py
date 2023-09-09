import sys
input = sys.stdin.readline
N = int(input())

arr = set([input().rstrip() for _ in range(N)])
arr = sorted(list(arr),key = lambda x : (len(x), x))

for i in arr:
    print(i)