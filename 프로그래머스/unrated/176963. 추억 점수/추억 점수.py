from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
    p_dict = defaultdict(int)
    for n, y in zip(name, yearning):
        p_dict[n] = y
        
    for p in photo:
        temp = 0
        for x in p:
            temp += p_dict[x]
        answer.append(temp)
        
    return answer