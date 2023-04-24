from itertools import combinations
N = int(input())
people = [i for i in range(N)]

graph = []
for _ in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)
    
def calculating(arr):
    total = 0
    while arr:
        x = arr.pop()
        if len(arr) >= 1:
            for y in arr:
                total += graph[x][y] + graph[y][x]
    return total    

answer = float('inf')
for i in range(1, N//2+1):
    for arr in list(combinations(people, i)):
        start = list(arr)
        link = list(set(people)-set(arr))
        start_sum = calculating(start)
        link_sum = calculating(link)
        answer = min(answer, abs(link_sum - start_sum))
        if answer == 0:
            break
print(answer)