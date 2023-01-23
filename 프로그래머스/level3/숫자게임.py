def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    while A:
        a = A.pop()
        for _ in B:
            b = B.pop()
            if b > a:
                answer += 1
                break
    return answer
