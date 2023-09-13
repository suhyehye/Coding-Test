import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
arr = [[INF] * (N+1) for _ in range(N+1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    arr[a][b] = 1
    arr[b][a] = 1
    
for i in range(N+1):
    arr[i][i] = 0
    
for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            arr[i][j] = min(arr[i][k]+arr[k][j], arr[i][j])

m_ans = INF
ans = []           
for i in range(1,N+1):
    temp = 0
    for j in range(1,N+1):
        temp = max(temp, arr[i][j])
    if temp == m_ans:
        ans.append(i)
    elif temp < m_ans:
        m_ans = temp
        ans = [i]
        
print(m_ans, len(ans))
print(*ans)