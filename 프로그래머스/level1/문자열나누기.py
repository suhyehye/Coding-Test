def solution(s):
    st = s[0]
    answer, cnt, n_cnt = 0, 1, 0
    for i in range(1,len(s)-1):
        if s[i] == st:
            cnt += 1
        else:
            n_cnt += 1
        if cnt == n_cnt:
            answer += 1
            cnt, n_cnt = 0, 0
            st = s[i+1]
    return answer+1
