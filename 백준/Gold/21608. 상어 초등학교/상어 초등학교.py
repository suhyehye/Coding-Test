N = int(input())
friends = dict()
for _ in range(N*N):
    f = list(map(int, input().split()))
    friends[f[0]] = f[1:]

desk = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x,y, student, like_frends):
    f_cnt = 0
    e_cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N : 
            if desk[nx][ny] in like_frends:
                f_cnt += 1
            elif desk[nx][ny] == 0:
                e_cnt += 1
    return f_cnt, e_cnt
        

for k, v in friends.items():
    result = []
    for x in range(N):
        for y in range(N):
            if desk[x][y] == 0:
                f_cnt, e_cnt = check(x, y, k, v)
                result.append([x, y, f_cnt, e_cnt])
                
    result.sort(key=lambda x: (x[2], x[3], -x[0], -x[1]), reverse=True)         
    desk[result[0][0]][result[0][1]] = k
        
ans = 0
for x in range(N):
    for y in range(N):
        cnt = 0
        student = desk[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and desk[nx][ny] in friends[student]:
                cnt += 1
        if cnt == 0:
            ans += 0
        elif cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000
print(ans)