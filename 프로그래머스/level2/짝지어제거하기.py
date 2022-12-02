def solution(s):
    ss = [s[0]]
    for i in s:
        if i != ss[-1]:
            ss.append(i)
    return ''.join(ss)
