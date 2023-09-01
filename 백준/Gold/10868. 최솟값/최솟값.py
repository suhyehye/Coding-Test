import sys
from math import ceil, log2

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def init(i, start, end):
    if start == end:
        tree[i] = arr[start]
        return tree[i]
    mid = (start+end) // 2
    tree[i] = min(init(i*2, start, mid), init(i*2+1, mid+1, end))
    return tree[i]

def search(i, start, end, left, right):
    if end < left or start > right:
        return 10**9+1
    elif start >= left and end <= right:
        return tree[i]
    mid = (start + end) // 2
    return min(search(i*2, start, mid, left, right), search(i*2+1, mid+1, end, left, right))

N, M = map(int, input().split())
tree = [0 for _ in range(int(pow(2,ceil(log2(N)+1)+1)))]
arr = [int(input()) for _ in range(N)]
init(1, 0, N-1)

for _ in range(M):
    a, b = map(int, input().split())
    print(search(1, 0, N-1, a-1, b-1))