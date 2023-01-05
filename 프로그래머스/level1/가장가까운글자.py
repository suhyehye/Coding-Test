from collections import defaultdict
def solution(s):
    answer = []
    s_dict = defaultdict(int)
    for idx,i in enumerate(s):
        if s_dict[i] == 0:
            answer.append(-1)
        else:
            answer.append(idx-s_dict[i]+1)
        s_dict[i] = idx+1
    return answer
