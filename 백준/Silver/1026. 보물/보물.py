import sys
input = sys.stdin.readline

N = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort(reverse=True)

ans = 0
for i in range(N):
    ans += a_list[i] * b_list[i]
print(ans)