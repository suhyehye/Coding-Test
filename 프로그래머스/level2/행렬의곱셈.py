import numpy as np
def solution(arr1, arr2):
    answer = []
    arr2_t = np.array(arr2).T
    arr2_t = [[int(i) for i in x] for x in arr2_t]
    
    for i in range(len(arr1)):
        a = []
        for j in range(len(arr2_t)):
            a.append(sum([x*y for x,y in zip(arr1[i],arr2_t[j])]))
        answer.append(a)    
    return answer
