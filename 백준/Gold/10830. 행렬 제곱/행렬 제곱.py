import sys
from copy import deepcopy
input = sys.stdin.readline

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def mat(n_arr, arr):
    return [[sum([x*y[j] for x,y in zip(n_arr[i], arr)]) % 1000 for j in range(n)] for i in range(n)]

n_arr = deepcopy(arr)

def devide(b, n_arr):
    if b == 1:  # b = 1이 될때까지 재귀
        return n_arr
    else:
        tmp = devide(b//2, n_arr)
        if b % 2 == 0:  # b가 짝수인 경우
            return mat(tmp, tmp)
        else:
            return mat(mat(tmp, tmp), n_arr)

res = devide(b, n_arr)

for i in res:
    for j in i:
        print(j % 1000, end=' ')
    print()