import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(1,N):
    for j in range(len(graph[i])):
        if j == 0:
            graph[i][j] += graph[i-1][j]
        elif j == len(graph[i]) - 1 :
            graph[i][j] += graph[i-1][j-1]
        else:
            graph[i][j] += max(graph[i-1][j], graph[i-1][j-1])
print(max(graph[-1]))