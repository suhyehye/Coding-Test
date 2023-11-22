from itertools import combinations
def solution(relation):
    answer = []
    k_list = [x for x in range(len(relation[0]))]
    keys = []
    for i in range(len(relation[0])):
        keys.extend(list(combinations(k_list, i)))
    
    flag = 0
    keys = keys[1:]
    while keys:
        key = keys.pop(0)
        tmp = [tuple(relation[j][i] for i in key) for j in range(len(relation))]
        if len(set(tmp)) == len(tmp):
            answer.append(key)
            
            n_keys = []
            for k in keys:
                for x in key:
                    if x not in k:
                        n_keys.append(k)
                        break
            keys = n_keys
        
    return len(answer) if answer else 1