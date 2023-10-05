import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    line, n = map(int, input().split())
    max_t, min_t = 0, 0
    for _ in range(n):
        ant = int(input())
        if ant > line - ant:
            max_t = max(max_t, ant)
            min_t = max(min_t, line-ant)
        else:
            max_t = max(line-ant, max_t)
            min_t = max(min_t, ant)
    print(min_t, max_t)