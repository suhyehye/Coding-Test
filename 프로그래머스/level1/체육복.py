def solution(n, lost, reserve):
    reserve2 = set(reserve) - set(lost)
    lost2 = set(lost) - set(reserve)
    for i in lost2:
        if i-1 in reserve2:
            reserve2.remove(i-1)
        elif i+1 in reserve2:
            reserve2.remove(i+1)
        else:
            n -= 1
    return n
