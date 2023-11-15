from collections import defaultdict
def solution(record):
    answer = []
    translate = {'Enter' : "님이 들어왔습니다.",
                'Leave' : "님이 나갔습니다."}
    name = defaultdict(str)
    
    for x in record:
        s = x.split(' ')
        if s[0] == 'Enter' or s[0] == 'Change':
            name[s[1]] = s[2]
        if s[0] == 'Enter' or s[0] == 'Leave':
            answer.append(s)
    
    res = []
    for x in answer:
        res.append(name[x[1]] + translate[x[0]])
    return res
