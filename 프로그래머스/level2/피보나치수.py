def solution(n):
    answer = [0,1]
    for i,x in enumerate(range(n-1),start=2):
        answer.append(answer[i-2]+answer[i-1])
    return answer[-1] % 1234567
