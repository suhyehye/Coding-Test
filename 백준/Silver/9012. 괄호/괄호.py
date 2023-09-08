import sys
from collections import deque
input = sys.stdin.readline
N = int(input())


for _ in range(N):
    string = list(input().rstrip())
    stack = []
    flag = True
    for i in string:
        if i == "(":
            stack.append(i)
            continue
        else:
            if stack == []:
                print("NO")
                flag = False
                break

            stack.pop()
    if flag:            
        if stack == []:
            print("YES")
        else:
            print("NO")