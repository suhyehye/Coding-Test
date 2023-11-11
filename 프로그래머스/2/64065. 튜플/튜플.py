import re
def solution(s):
    answer = []
    s = re.split(r"{|}", s)
    s = [re.findall(r"\d+", x) for x in s if x!="" and x != ","]
    s = sorted(s, key = lambda x:len(x))
    for x in s:
        for y in x:
            if int(y) not in answer:
                answer.append(int(y))
    return answer