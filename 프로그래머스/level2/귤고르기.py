from collections import Counter
def solution(k, tangerine):
    count_list = Counter(tangerine)
    tangerine=sorted(tangerine,key=lambda x : (count_list[x],x),reverse=True)
    return len(set(tangerine[:k]))
