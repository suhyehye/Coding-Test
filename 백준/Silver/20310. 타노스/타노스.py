S = list(input().strip())

c0 = S.count("0") // 2
c1 = S.count("1") // 2

cnt0 = 0
cnt1 = 0

for _ in range(c0):
    S.pop(-(S[::-1].index("0")) - 1)

for _ in range(c1):
    S.pop(S.index("1"))

print("".join(S))   