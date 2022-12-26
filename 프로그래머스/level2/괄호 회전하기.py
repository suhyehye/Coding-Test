from collections import deque
def solution(s):
    answer = 0
    s= deque(s)
    s.rotate(1)
    left = ['[', '(', '{']
    right = [']',')', '}']
    for i in range(len(s)):
        s.rotate(-1)
        stack = []
        answer += 1
        for x in s:
            if x in left:
                stack.append(x)
            elif left[right.index(x)] not in stack:
                answer -= 1
                break
            elif left[right.index(x)] == stack[-1]:
                stack.pop()
            else:
                answer -=1
                break
        if stack != []:
            answer -=1
    return max(answer,0)
