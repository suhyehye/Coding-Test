import sys
input = sys.stdin.readline

N, L = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
def check_r(i):
    j = 1
    runways = []
    while j < N:
        if maps[i][j-1] == maps[i][j]:
            j += 1
            continue
        elif maps[i][j-1] - maps[i][j] == 1 and j + L - 1 <= N - 1 and [i,j] not in runways:
            temp = maps[i][j]
            runways.append([i,j])
            for x in range(j+1, j+L):
                if temp != maps[i][x] or [i,x] in runways: 
                    return 0
                runways.append([i,x])
            j += 1
        elif maps[i][j-1] - maps[i][j] == -1 and j - L >= 0 and [i,j-1] not in runways :
            temp = maps[i][j-1]
            runways.append([i,j-1])
            for x in range(j-2, j-L-1, -1):
                if temp != maps[i][x] or [i,x] in runways:
                    return 0
                runways.append([i,x])
            j += 1
        else:
            return 0
    return 1
                
def check_c(i):
    j = 1
    runways = []
    while j < N:
        if maps[j-1][i] == maps[j][i]:
            j += 1
            continue
        elif maps[j-1][i] - maps[j][i] == 1 and j + L - 1 <= N - 1 and [j,i] not in runways:
            temp = maps[j][i]
            runways.append([j,i])
            for x in range(j+1, j+L):
                if temp != maps[x][i] or [x,i] in runways: 
                    return 0
                runways.append([x,i])
            j += 1
        elif maps[j-1][i] - maps[j][i] == -1 and j - L >= 0 and [j-1, i] not in runways :
            temp = maps[j-1][i]
            runways.append([j-1, i])
            for x in range(j-2, j-L-1, -1):
                if temp != maps[x][i] or [x,i] in runways:
                    return 0
                runways.append([x,i])
            j += 1
        else:
            return 0
    return 1          
   
for i in range(N):
    cnt += check_r(i)
    cnt += check_c(i)

print(cnt)