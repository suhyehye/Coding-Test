from collections import defaultdict
from itertools import product
def solution(user_id, banned_id):
    arr = []
    for ban in banned_id:
        tmp = set()
        idx = [i for i,x in enumerate(ban) if x == '*']
        for uid in user_id:
            n_uid = ''.join([x if i not in idx else '*' for i,x in enumerate(uid)])
            if n_uid == ban:
                tmp.add(uid)
        arr.append(tmp)

    arr = list(product(*arr))    
    arr = set([tuple(sorted(x)) for x in arr if len(set(x)) == len(x)])
    return len(arr)