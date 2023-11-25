import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = {}
for _ in range(n):
    site, pw = input().rstrip().split()
    data[site] = pw
    
for _ in range(m):
    x = input().rstrip()
    print(data[x])