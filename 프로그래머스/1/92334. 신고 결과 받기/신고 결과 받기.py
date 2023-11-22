from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    count = defaultdict(int)    # 각 유저별 신고당한 횟수
    reporter = defaultdict(set)    # 각 유저별 신고한 유저 set
    
    for x in set(report):
        a, b = x.split(' ')
        count[b] += 1
        reporter[a].add(b)
    
    mail = []
    for key, v in count.items():
        if v >= k:
            mail.append(key)
    
    for user in id_list:
        tmp = 0
        for x in reporter[user]:
            if x in mail:
                tmp += 1
        answer.append(tmp)
    return answer