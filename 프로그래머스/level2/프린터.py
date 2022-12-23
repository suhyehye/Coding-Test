from collections import deque
def solution(priorities, location):
    priorities = deque([[idx, x] for idx, x in enumerate(priorities)])
    waiting = []
    
    while len(priorities) >= 1:
        i = priorities.popleft()
        if len(priorities) == 0:
            waiting.append(i)
        elif i[1] < max([x[1] for x in priorities]):
            priorities.append(i)
        else:
            waiting.append(i[0])
            if i[0] == location:
                break
    return len(waiting)
