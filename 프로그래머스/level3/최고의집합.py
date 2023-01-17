def solution(n, s):
    if s//n < 1:
        return [-1]
    
    answer = []
    while s >= 0:
        if s % n == 0:
            answer.extend([s//n for _ in range(n)])
            break
        else:
            answer.append(s//n+1)
            s = s - s//n -1
            n -= 1
            
    return sorted(answer)
