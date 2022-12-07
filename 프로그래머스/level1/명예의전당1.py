def solution(k, score):
    answer = []
    for i in range(1,len(score)+1):
        if i <= k:
            answer.append(min(score[:i]))
        else:
            answer.append(sorted(score[:i],reverse=True)[k-1])
    return answer
