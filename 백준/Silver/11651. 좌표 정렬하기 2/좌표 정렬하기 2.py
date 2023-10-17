import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))

for i in arr:
    print(*i)