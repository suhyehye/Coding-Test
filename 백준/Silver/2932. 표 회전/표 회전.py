N, K = map(int, input().split())
arr = []
for _ in range(K):
    n, x, y = map(int, input().split())
    arr.append([n, x-1, y-1, (n-1)//N, (n-1)%N])

def rotate_row(i, col, idx):
    for k in range(idx, K):
        if arr[k][3] == col:
            arr[k][4] = (arr[k][4]+i) % N

def rotate_col(i, row, idx):
    for k in range(idx, K):
        if arr[k][4] == row:
            arr[k][3] = (arr[k][3]+i) % N
    
def calculate(xy, nxy):
    if nxy >= xy:
        return nxy - xy
    else:
        return N - (xy - nxy)
        
for idx, ar in enumerate(arr):
    num, nx, ny, x, y = ar[0], ar[1], ar[2], ar[3], ar[4]
    x_turn = calculate(x, nx)
    y_turn = calculate(y, ny)
    rotate_row(y_turn, x, idx)
    rotate_col(x_turn, ny, idx)
    print(x_turn + y_turn)