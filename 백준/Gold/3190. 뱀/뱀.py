import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())

arr = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

X = int(input())
times = sorted([input().split() for _ in range(X)], key=lambda x:int(x[0]))
dirs = [[0,1], [1,0], [0,-1], [-1,0]]
d, t = 0, 0
snail = deque()
snail.append([0,0])

def move(d,time):
    global t
    while t < time : 
        t += 1
        nx = snail[0][0] + dirs[d][0]
        ny = snail[0][1] + dirs[d][1]
        if nx >= N or nx < 0 or ny >= N or ny < 0 or [nx,ny] in snail:
            print(t)
            exit()
        elif arr[nx][ny] == 0:
            snail.appendleft([nx,ny])
            snail.pop()
        elif arr[nx][ny] == 1:
            arr[nx][ny] = 0
            snail.appendleft([nx,ny])
    
for i in times:
    move(d, int(i[0]))
    if i[1] == "D":
        d = (d+1) % 4
    else:
        d = (d+3) % 4
        
move(d, sys.maxsize)