N = int(input())
ans = 0
def check(word):
    stack = []
    for i in word:
        if i not in stack:
            stack.append(i)
        elif i != stack[-1]:
            return 0
    return 1

for _ in range(N):
    ans += check(input())
print(ans)