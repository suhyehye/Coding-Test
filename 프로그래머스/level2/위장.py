from collections import defaultdict
def solution(clothes):
    answer = 1
    cloth_dict = defaultdict(int)
    for i in clothes:
        cloth_dict[i[1]] += 1
    
    for v in cloth_dict.values():
        answer = answer * (v+1)
    return answer-1
