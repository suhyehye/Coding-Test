from math import comb
def solution(n):
    answer = 1
    cnt = 0
    while cnt <= n//2:
        cnt+=1
        answer += comb(n-cnt,cnt)
    return answer % 1234567
