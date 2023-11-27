import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    tmp, idx = 0, 0
    for x in a:
        while idx < m and b[idx] < x:
            idx += 1
            
        tmp += idx
    print(tmp)