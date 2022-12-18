import math

def solution(progresses, speeds):
    a=[math.ceil((100-progresses[p])/speeds[p]) for p in range(len(progresses))]
    answer = [1]
    big = a[0]
    
    for i in range(1,len(a)):
        if big >= a[i]:
            answer[-1] = answer[-1]+1
        else:
            big = a[i]
            answer.append(1)
    return answer
