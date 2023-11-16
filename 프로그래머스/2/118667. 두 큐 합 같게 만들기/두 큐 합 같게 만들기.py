from collections import deque
def solution(queue1, queue2):
    cnt = 0
    q1, q2 = deque(queue1), deque(queue2)
    t1, t2 = sum(q1), sum(q2)
    total = t1 + t2
    if total % 2 :
        return -1
    
    while q1 and q2 and t1 != total // 2 and t2 != total // 2 and cnt < 4*len(queue1):
        cnt += 1
        if t1 > t2:
            x = q1.popleft()
            q2.append(x)
            t1 -= x
            t2 += x
        else:
            x = q2.popleft()
            q1.append(x)
            t2 -= x
            t1 += x
    
    return cnt if t1 == t2 else -1