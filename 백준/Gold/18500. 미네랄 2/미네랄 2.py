from collections import deque, defaultdict

R, C = map(int, input().split())

graph = []
for i in range(R):
    tmp = list(input().rstrip())
    graph.append(tmp)

N = int(input())
heights = list(map(int, input().split()))
# graph 인덱스와 맞춤
heights = [x-1 for x in heights]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start_x, start_y, graph):
    graph[start_y][start_x] = "."
    # 미네랄을 이동해야하는지 여부 확인
    
    v_dict = defaultdict(list)
    visited = [[0] * C for _ in range(R)]
    q = deque()
    idx = 0
    
    for y in range(R):
        for x in range(C):
            if graph[y][x] == "x" and visited[y][x] == 0:
                q.append([x, y])
                idx += 1
                v_dict[idx].append([x, y])
                visited[y][x] = 1
            
                while q:
                    x, y = q.pop()
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] == "x" and visited[ny][nx] == 0:
                            q.append([nx, ny])
                            v_dict[idx].append([nx, ny])
                            visited[ny][nx] = 1
                            
    return v_dict

def move(graph, visited):
    # 미네랄을 옮기는 함수
    if visited is None:
        return graph
        
    max_y_list = []
    for idx, v in visited.items():
        v = sorted(v, key=lambda x:x[1], reverse=True)
        visited[idx] = v
        max_y_list.append((idx, v[0][1]))
    
    max_y_list.sort(key=lambda x:x[1], reverse=True)

    for idx, max_y in max_y_list:
        flag = True
        for x, y in visited[idx]:
            if y  == R-1:
                flag = False
                break
            if y == max_y and y+1 <= R-1 and graph[y+1][x] == "x":
                flag = False
                break
            if y < max_y:
                break

        cnt = 1
        while flag:
            for x, y in visited[idx]:
                if y+cnt == R-1 or ([x, y+cnt+1] not in visited[idx] and graph[y+cnt+1][x] == "x"):
                    flag = False
                    break
                    
            if flag == False:
                for x, y in visited[idx]:
                    graph[y][x] = "."
                    graph[y+cnt][x] = "x"
                
                break
            cnt += 1   
            
    return graph            

for i in range(N):
    h = heights[i]
    y = R - h - 1
    
    # 왼쪽 -> 오른쪽
    if i%2 == 0:
        for x in range(C):
            if graph[y][x] == "x":
                # 미네랄인 경우 
                graph[y][x] = "."
                visited = bfs(start_x=x, start_y=y, graph=graph)
                # print(f"i : {i}, x : {x}, y : {y}, graph[y][x] : {graph[y][x]}, flag : {flag}")
                graph = move(graph=graph, visited=visited)
                break
    
    else:
        for x in range(C-1, -1, -1):
            if graph[y][x] == "x":
                graph[y][x] = "."
                visited = bfs(start_x=x, start_y=y, graph=graph)
                # print(f"i : {i}, x : {x}, y : {y}, graph[y][x] : {graph[y][x]}, flag : {flag}")
                graph = move(graph=graph, visited=visited)
                break
            
for x in graph:
    print(''.join(x))