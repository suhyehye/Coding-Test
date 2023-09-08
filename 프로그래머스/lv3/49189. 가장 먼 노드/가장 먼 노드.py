from collections import deque
def solution(n, edge):
    answer = [-1 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    q = deque([1])
    answer[1] = 0
    while q:
        x = q.popleft()
        for v in graph[x]:
            if answer[v] == -1:
                q.append(v)
                answer[v] = answer[x] + 1
    return answer.count(max(answer))