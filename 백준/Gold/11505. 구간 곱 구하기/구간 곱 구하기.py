import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline
MOD = 1000000007

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    
    mid = (start + end) // 2
    tree[node] = (init(node*2, start, mid) * init(node*2+1, mid+1, end)) % MOD
    return tree[node]

def update(node, start, end, index, val):
    if index < start or index > end:
        return tree[node]
    
    if start == end:
        tree[node] = val
        return tree[node]
    
    mid = (start + end) // 2
    left_val = update(node*2, start, mid, index, val)
    right_val = update(node*2+1, mid+1, end, index, val)
    tree[node] = (left_val * right_val) % MOD
    return tree[node]
    
def query(node, start, end, left, right):
    if left > end or right < start:
        return 1
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    left_res = query(node*2, start, mid, left, right)
    right_res = query(node*2+1, mid+1, end, left, right)
    
    return (left_res * right_res) % MOD
        

N, K, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

tree = [0] * (N*4)
init(1, 0, N-1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b-1] = c
        update(1, 0, N-1, b-1, c)
    else:
        print(query(1, 0, N-1, b-1, c-1))