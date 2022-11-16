from itertools import product
def solution(A,B):
    A.sort(), B.sort(reverse=True)
    pr = [i*j for i,j in zip(A,B)]
    answer = 0
    
    for i in pr:
        answer += i
    return answer
