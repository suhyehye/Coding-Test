from collections import defaultdict
from itertools import combinations

def solution(friends, gifts):
    friends_dict = defaultdict(list)
    gift_score = defaultdict(int)
    friends_list = []
    for gift in gifts:
        a, b = gift.split(" ")
        friends_dict[a].append(b)
        gift_score[a] += 1
        gift_score[b] -= 1
    
    gift_dict = defaultdict(int)
    print(friends_dict)
    for comb in combinations(friends, 2):
        if friends_dict[comb[0]].count(comb[1]) > friends_dict[comb[1]].count(comb[0]):
            gift_dict[comb[0]] += 1
        elif friends_dict[comb[1]].count(comb[0]) > friends_dict[comb[0]].count(comb[1]):
            gift_dict[comb[1]] += 1
        elif gift_score[comb[0]] > gift_score[comb[1]]:
            gift_dict[comb[0]] += 1
        elif gift_score[comb[1]] > gift_score[comb[0]]:
            gift_dict[comb[1]] += 1
        else:
            pass
    if gift_dict.values():
        return max(gift_dict.values())
    return 0