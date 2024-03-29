def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(len(score)//m):
        price = score[i*m:i*m+m][-1] * m
        answer += price
    return answer
