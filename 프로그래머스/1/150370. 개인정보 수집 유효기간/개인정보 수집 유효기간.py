def solution(today, terms, privacies):
    answer = []
    y, m, d = map(int, today.split('.'))
    today = (y-2000)*28*12 + m*28 + d
    terms = dict([x.split() for x in terms])
    
    for idx, p in enumerate(privacies):
        day, t = p.split(' ')
        y, m, d = map(int, day.split('.'))
        day = (y-2000)*28*12 + m*28 + d
        if day + int(terms[t]) * 28 <= today:
            answer.append(idx+1)
    return answer