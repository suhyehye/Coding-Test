import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def rotate(arr):
    n_arr = [[0]*M for _ in range(N)]
    for k in range(min(N, M)//2):
        for j in range(k,M-k):
            if j == M-k-1:
                n_arr[k][j] = arr[k+1][j]
                n_arr[N-k-1][j] = arr[N-k-1][j-1]
            elif j == k:
                n_arr[N-k-1][j] = arr[N-k-2][j]
                n_arr[k][j] = arr[k][j+1]
            else:
                n_arr[k][j] = arr[k][j+1]
                n_arr[N-k-1][j] = arr[N-k-1][j-1]
                
        # 왼쪽
        for i in range(k,N-k):
            if i == k:
                n_arr[i][k] = arr[i][k+1]
                n_arr[i][M-k-1] = arr[i+1][M-k-1]
                
            elif i == N-k-1:
                n_arr[i][M-k-1] = arr[i][M-k-2]
                n_arr[i][k] = arr[i-1][k]
            else:
                n_arr[i][k] = arr[i-1][k]
                n_arr[i][M-k-1] = arr[i+1][M-k-1]
    return n_arr

for _ in range(R):
    arr = rotate(arr)

for i in arr:
    print(*i)