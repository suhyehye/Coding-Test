import sys
from math import ceil, pow, log2

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for i in range(N)]

def init(arr, tree, i, left, right):
    if left == right:
        tree[i] = [arr[left], arr[left]]
        return tree[i]
    mid = (left + right) // 2
    l_ar = init(arr, tree, i*2, left, mid) 
    r_ar = init(arr, tree, i*2+1, mid+1, right) 
    tree[i] = [min(l_ar[0], r_ar[0]), max(l_ar[1], r_ar[1])]
    return tree[i]
    
h = ceil(log2(N)) + 1 # 노드 개수에 따른 트리의 높이 계산 공식
nodeNum = 1 << h ## 2^h 계산
tree = [0 for _ in range(nodeNum)]
init(arr, tree, 1, 0, N-1)

def search(tree, i, start, end, left, right):
    if end < left or right < start:
        return [10**9+1,0]
    if left <= start and right >= end:
        return tree[i]
    mid = (start+end) // 2
    l_ar = search(tree, i*2, start, mid, left, right)
    r_ar = search(tree, i*2+1, mid+1, end, left, right)
    return min(l_ar[0], r_ar[0]), max(l_ar[1], r_ar[1])

for _ in range(M):
    a, b = map(int, input().split())
    min_x, max_x = search(tree, 1, 0, N-1, a-1, b-1)
    print(min_x, max_x)