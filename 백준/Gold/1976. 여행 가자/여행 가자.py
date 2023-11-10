import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [x for x in range(n+1)]

def find(x):
    if graph[x] != x:
        graph[x] = find(graph[x])
        return graph[x]
    return x

def union(x, y):
    x, y = find(x), find(y)
    graph[x] = y
    
for i in range(1, n+1):
    tmp = [0] + list(map(int, input().split()))
    for j in range(i+1, len(tmp)):
        if tmp[j] == 1:
            union(i, j)
            
for i in range(1, n+1):
    find(i)
        
arr = list(map(int, input().split()))
start = graph[arr[0]]

for i in range(1, m):
    if start != graph[arr[i]]:
        print("NO")
        exit()
        
print("YES")