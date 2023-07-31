import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

notebook = [[0] * M for _ in range(N)]

def rotate(arr):
    result = zip(*arr[::-1])
    return [list(i) for i in result]

def check(sticker):
    for x in range(len(sticker)):
        for y in range(len(sticker[0])):
            if sticker[x][y] + notebook[i+x][j+y] > 1:
                return False
            
    for x in range(len(sticker)):
        for y in range(len(sticker[0])):
            if sticker[x][y] == 1:
                notebook[i+x][j+y] = 1
    return True

    
for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    cnt = 0
    chk = False
    while cnt < 4:
        if chk == True:
            break
        for i in range(N-len(sticker)+1):
            if chk == True:
                break
            for j in range(M-len(sticker[0])+1):
                if check(sticker) == True:
                    chk = True
                    break
            
        sticker = rotate(sticker)
        cnt += 1
        
answer = 0
for i in range(N):
    for j in range(M):
        if notebook[i][j] == 1:
            answer += 1
            
print(answer)