import sys
N = int(input())
# 첫번째는 양수, 두번째는 0보다 작은 수
ar1, ar2 = [], []
for _ in range(N):
    i = int(sys.stdin.readline())
    if i > 0:
        ar1.append(i)
    else:
        ar2.append(i)
ar1.sort()
ar2.sort(reverse=True)

ans = 0
while len(ar1) > 0:
    x = ar1.pop()
    if len(ar1) == 0:
        ans += x
        break
    elif x * ar1[-1] > x and x*ar1[-1] >= ar1[-1]:
        x2 = ar1.pop()
        ans += x * x2
    else:
        ans += x
while len(ar2) > 0:
    x = ar2.pop()
    if len(ar2) == 0:
        ans += x
        break
    elif x * ar2[-1] > x and x*ar2[-1] >= ar2[-1]:
        x2 = ar2.pop()
        ans += x * x2
    else:
        ans += x
print(ans)