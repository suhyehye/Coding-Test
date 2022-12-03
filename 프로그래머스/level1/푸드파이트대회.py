def solution(food):
    answer = ''
    for i, f in enumerate(food[1:]):
        fo = f//2
        answer += str(i+1) * fo
    
    return answer+'0'+answer[::-1]
