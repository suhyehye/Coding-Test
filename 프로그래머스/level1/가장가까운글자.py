import numpy as np
def solution(s):
    answer = []
    s_stack = []
    for idx,i in enumerate(s):
        if i in s_stack:
            answer.append(idx - int(np.where(np.array(s_stack) == i)[-1][-1]))
        else:
            answer.append(-1)
        s_stack.append(i)
    return answer
