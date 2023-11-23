def solution(n, s, a, b, fares):
    answer = int(1e9)
    visited = [[int(1e9)] * (n+1) for _ in range(n+1)]
    
    for fare in fares:
        visited[fare[0]][fare[1]] = fare[2]
        visited[fare[1]][fare[0]] = fare[2]
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                visited[i][j] = min(visited[i][j], visited[i][k] + visited[k][j])
                
    for i in range(1, n+1):
        visited[i][i] = 0
        
    for x in range(1, n+1):
        answer = min(visited[s][x] + visited[x][a] + visited[x][b], answer)
    return answer