def solution(s):
    ss = ['0']
    for i in s:
        if i != ss[-1]:
            ss.append(i)

        else:
            ss.pop(-1)
            
    if ''.join(ss[1:]) == '':
        return 1
    else:
        return 0
