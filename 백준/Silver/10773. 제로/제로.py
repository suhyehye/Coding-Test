import sys
input = sys.stdin.readline
N = int(input())

stack = []
for _ in range(N):
    x = int(input())
    if x == 0 and stack != []:
        stack.pop()
    else:
        stack.append(x)
print(sum(stack))