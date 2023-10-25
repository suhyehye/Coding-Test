import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    x = input().rstrip()
    tmp = 0
    
    for xx in x:
        if xx.isdigit():
            tmp += int(xx)
    data.append([x, tmp])

data.sort(key = lambda x:(len(x[0]), x[1], x[0]))

for x in data:
    print(x[0])