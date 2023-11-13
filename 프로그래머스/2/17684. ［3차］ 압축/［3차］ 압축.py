from collections import defaultdict
def solution(msg):
    answer = []
    aa = defaultdict(int)
    for i in range(1,27):
        aa[chr(i+64)] = i
    
    cnt = 26
    idx = 0
    
    while idx < len(msg):
        for i in range(2, len(msg)):
            if aa[msg[idx:idx+i]] == 0:
                break
        cnt += 1
        answer.append(aa[msg[idx:idx+i-1]])
        aa[msg[idx:idx+i]] = cnt
        idx += i - 1
        
    return answer