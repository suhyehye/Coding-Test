import re
def solution(dartResult):
    answer = []
    scores = re.compile(r'([0-9]|10)([SDT])([*#]?)').findall(dartResult)
    for s in scores:
        tmp = int(s[0])
        if s[1] == "D":
            tmp = tmp ** 2
        if s[1] == 'T':
            tmp = tmp ** 3
        if s[2] == '*':
            if answer:
                answer[-1] = answer[-1] * 2
            tmp *= 2
        if s[2] == '#':
            tmp *= -1
        
        answer.append(tmp)
    return sum(answer)