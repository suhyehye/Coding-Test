def solution(s):
    answer = 1001
    if len(s) == 1:
        return 1
    
    for i in range(1,len(s)//2+1):
        new_s, tmp = '', ''
        cnt = 1
        for j in range(len(s)//i+1):
            if tmp == s[j*i:j*i+i]:
                cnt += 1
            else:
                if cnt > 1:
                    new_s += str(cnt) + tmp
                else:
                    new_s += tmp
                cnt = 1
                tmp = s[j*i:j*i+i]
        new_s += tmp
        answer = min(len(new_s), answer)
    return answer