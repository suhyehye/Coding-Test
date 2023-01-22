from collections import deque

def bfs(computers, start, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 0
    while queue:
        v = queue.popleft()
        for i in range(len(computers[v])):
            if i != v and not visited[i] and computers[v][i] == 1:
                queue.append(i)
                cnt += 1
                visited[i] = True
    return cnt
                
def solution(n, computers):
    answer = n
    visited = [False] * n
    for x in range(n):
        if not visited[x]:
            answer -= bfs(computers,x,visited)
    return answer
