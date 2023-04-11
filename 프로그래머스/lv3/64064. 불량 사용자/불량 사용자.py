import numpy as np
from itertools import product
def solution(user_id, banned_id):
    answer = []
    for id in banned_id:
        
        # "*"처리된 인덱스를 담을 리스트 선언
        star = []
        ids = []
        for i,x in enumerate(id):
            if x == '*':
                star.append(i)
        
        for u_id in user_id:
            if len(u_id) == len(id):
                new_id = u_id
                for s in star:
                    new_id = new_id[:s] + '*'+ new_id[s+1:]
                if new_id == id:
                    ids.append(u_id)
                    
        answer.append(ids)
    
    answer = list(product(*answer))
    answer = [sorted(x) for x in answer if len(x) == len(set(x))]
    answer = set(list(map(tuple,answer)))
    
    return len(answer)