import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if i == n-1 and j == m-1:
            continue
        else:
            temp = []
            if i + 1 < n:
                temp.append(arr[i+1][j])
            if j + 1 < m:
                temp.append(arr[i][j+1])
            arr[i][j] += max(temp)

print(arr[0][0])